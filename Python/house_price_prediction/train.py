"""Beginner-friendly Bengaluru house-price training and submission script."""

# Imports: pandas handles tables, NumPy handles math, sklearn builds the model.
import json
import re
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


# File locations. Change TEST_FILE if your test CSV is in a different folder.
ROOT = Path(__file__).resolve().parents[2]
TRAIN_FILE = ROOT / "train_(2)_(1)_(1)_(1).csv"
TEST_FILE = Path.home() / "Downloads" / "test_(2)_(1)_(1)_(1).csv"
SUBMISSION_FILE = ROOT / "submission.csv"
ARTIFACTS = Path(__file__).resolve().parent / "artifacts"

# Columns used by the model after feature engineering.
NUMBER_COLUMNS = ["total_sqft", "bhk", "bath", "balcony", "sqft_per_bhk", "bath_per_bhk", "ready_to_move"]
CATEGORY_COLUMNS = ["area_type", "location"]


def parse_total_sqft(value):
    """Turn values such as '2100 - 2850' into one square-foot number."""
    if pd.isna(value):
        return np.nan

    text = str(value).lower().replace(",", "")
    numbers = re.findall(r"\d+(?:\.\d+)?", text)
    if not numbers:
        return np.nan

    # When the value is a range, use its midpoint.
    area = sum(float(number) for number in numbers) / len(numbers)

    # Convert common area units to square feet.
    if "meter" in text:
        area *= 10.7639
    elif "yard" in text:
        area *= 9
    elif "acre" in text:
        area *= 43560
    return area


def add_features(frame):
    """Clean a listing table and add a few useful house-size features."""
    frame = frame.copy()
    frame["total_sqft"] = frame["total_sqft"].apply(parse_total_sqft)
    frame["bhk"] = frame["size"].astype("string").str.extract(r"(\d+)")[0].astype(float)
    frame["sqft_per_bhk"] = frame["total_sqft"] / frame["bhk"].replace(0, np.nan)
    frame["bath_per_bhk"] = frame["bath"] / frame["bhk"].replace(0, np.nan)
    frame["ready_to_move"] = (
        frame["availability"].fillna("").astype(str).str.lower().str.contains("ready to move").astype(int)
    )
    frame["area_type"] = frame["area_type"].fillna("unknown").astype(str).str.strip().str.lower()
    frame["location"] = frame["location"].fillna("unknown").astype(str).str.strip().str.lower()
    return frame


def main():
    # Read the labeled examples. Price is the value the model must learn to predict.
    train = add_features(pd.read_csv(TRAIN_FILE))
    train["price"] = pd.to_numeric(train["price"], errors="coerce")

    # Keep rows with a real price and a usable floor area.
    train = train[(train["price"] > 0) & (train["total_sqft"] > 0)].copy()

    # Remove exact repeats, but ignore ID because each row has a different identifier.
    duplicate_columns = [column for column in train.columns if column != "ID"]
    train = train.drop_duplicates(subset=duplicate_columns).copy()

    # X is the input; y is the known price. ID and society are intentionally excluded.
    X = train[NUMBER_COLUMNS + CATEGORY_COLUMNS]
    y = train["price"]

    # Hold out 20% so we can estimate how well the model predicts unseen homes.
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Fill missing numbers with medians. Trees do not need numeric scaling.
    number_steps = SimpleImputer(strategy="median")

    # Fill missing text and turn categories such as locality into numeric columns.
    category_steps = Pipeline(
        steps=[
            ("fill_missing", SimpleImputer(strategy="constant", fill_value="unknown")),
            ("one_hot", OneHotEncoder(handle_unknown="infrequent_if_exist", min_frequency=20, sparse_output=False)),
        ]
    )

    # Apply the right preparation to each type of feature.
    prepare = ColumnTransformer(
        transformers=[
            ("numbers", number_steps, NUMBER_COLUMNS),
            ("categories", category_steps, CATEGORY_COLUMNS),
        ]
    )

    # Histogram Gradient Boosting had the best holdout RMSE in our model comparison.
    model = Pipeline(
        steps=[
            ("prepare", prepare),
            ("regression", HistGradientBoostingRegressor(
                max_iter=250, learning_rate=0.07, max_leaf_nodes=31,
                l2_regularization=1, random_state=42
            )),
        ]
    )

    # Prices are skewed, so train on log(price); convert predictions back before scoring.
    model.fit(X_train, np.log1p(y_train))
    valid_prices = np.maximum(np.expm1(model.predict(X_valid)), 0)
    rmse = np.sqrt(mean_squared_error(y_valid, valid_prices))
    print(f"Holdout RMSE: {rmse:.2f} lakh rupees")

    # Refit on all labeled houses so the final model uses every training row.
    model.fit(X, np.log1p(y))
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, ARTIFACTS / "bengaluru_house_price.joblib")

    # Prepare the unlabeled secondary/test data using the same feature steps.
    test = add_features(pd.read_csv(TEST_FILE))
    test_X = test[NUMBER_COLUMNS + CATEGORY_COLUMNS]
    test_prices = np.maximum(np.expm1(model.predict(test_X)), 0)

    # Keep the test IDs and match the sample submission's two-column header.
    submission = pd.DataFrame({"ID": test["ID"], "price": test_prices})
    submission.to_csv(SUBMISSION_FILE, index=False)

    # Save a small report so the validation score and row counts are easy to find.
    report = {
        "model": "HistGradientBoostingRegressor",
        "holdout_rmse_lakh": float(rmse),
        "training_rows": int(len(train)),
        "test_rows": int(len(test)),
        "submission_columns": submission.columns.tolist(),
    }
    (ARTIFACTS / "metrics.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Training rows: {len(train)}")
    print(f"Submission saved to: {SUBMISSION_FILE}")
    print("Submission columns:", submission.columns.tolist())


if __name__ == "__main__":
    main()

