# Beginner walkthrough for `train.py`

`train.py` now keeps the learning flow short: read the labeled data, make features, prepare columns, train one regressor, score it with RMSE, refit on all labeled rows, and write predictions for the test rows.

## 1. Imports and file names

- `json` writes the small metrics report; `re` extracts numbers from area strings; `Path` builds file paths.
- `joblib` saves the trained model. NumPy supplies missing values, log transforms, and numeric calculations. Pandas reads and writes CSV tables.
- `ColumnTransformer` sends numeric and text columns through different preparation steps.
- `HistGradientBoostingRegressor` is the chosen regression model. It performed best by holdout RMSE in the earlier model comparison.
- `SimpleImputer` fills missing data; `mean_squared_error` is used to calculate RMSE; `train_test_split` creates the validation set.
- `Pipeline` chains preprocessing and model fitting so validation and test data get the same transformations.
- `OneHotEncoder` changes categories such as locality into numeric columns that the model can use.
- `ROOT` finds the repository root from this script's location. `TRAIN_FILE`, `TEST_FILE`, and `SUBMISSION_FILE` point to the two data files and final output. Edit `TEST_FILE` if the test file is not in Downloads.
- `ARTIFACTS` is the folder where the saved model and report go.
- `NUMBER_COLUMNS` and `CATEGORY_COLUMNS` are lists that define which engineered columns are numeric and which are text categories.

## 2. Convert area strings: `parse_total_sqft`

- The function receives one area value from the CSV.
- `pd.isna` catches blank areas; `np.nan` lets the later imputer handle missing values.
- The value is converted to lowercase text and commas are removed so `1,200` is easier to read.
- `re.findall` extracts every number. If there is no number, the function returns missing.
- The `area` calculation averages the numbers. For an area range such as `2100 - 2850`, that gives its midpoint.
- The `if` / `elif` block converts square meters, square yards, and acres to square feet. Values without a recognized unit are assumed to already be square feet.
- `return area` sends the cleaned numeric value back to the table.

## 3. Create house features: `add_features`

- `.copy()` avoids changing the original table while we add columns.
- `.apply(parse_total_sqft)` cleans the messy area values one row at a time.
- The `size` text is searched for a number, so `2 BHK`, `4 Bedroom`, and `1 RK` become numeric bedroom counts.
- `sqft_per_bhk` divides area by bedrooms. Zero bedrooms are replaced by missing first, preventing division by zero.
- `bath_per_bhk` adds another useful ratio: bathrooms per bedroom.
- The availability text becomes `ready_to_move`: 1 when the text says “ready to move”, otherwise 0.
- Missing area types and locations become `unknown`. Text is trimmed and lowercased so spelling differences in case or extra spaces do not create extra categories.
- `return frame` gives back the table containing the original fields plus engineered features.

## 4. Read and clean training data: `main`

- `pd.read_csv(TRAIN_FILE)` reads the labeled examples, and `add_features` prepares their input columns.
- `pd.to_numeric(..., errors="coerce")` makes `price` numeric; invalid text becomes missing.
- The filter keeps rows with a positive price and usable positive area. A model cannot learn from an absent label or invalid area.
- `duplicate_columns` lists every column except `ID`. Two identical examples with different IDs should count as one, while examples with different prices are retained.
- `drop_duplicates` removes only exact repeated examples based on that list.
- `X` is the set of input features. `y` is the target value, house price. `ID` is excluded because it is only a row label; `society` is excluded because it is often blank and has many unique names.

## 5. Holdout and preprocessing

- `train_test_split` sets aside 20% of the labeled examples as validation data. The fixed `random_state` makes the split repeatable.
- `SimpleImputer(strategy="median")` fills missing numbers using medians learned from the training portion. Median is less affected by very large homes than a mean.
- The category `Pipeline` fills missing text with `unknown`, then one-hot encodes each category.
- `handle_unknown="infrequent_if_exist"` lets a new test locality be processed even if it was absent from training. `min_frequency=20` groups rare categories to reduce overfitting. `sparse_output=False` creates the dense input required by this tree model.
- `ColumnTransformer` applies the numeric imputer only to the numeric columns and the category pipeline only to area type and location.
- The model `Pipeline` chains this preparation with `HistGradientBoostingRegressor`. A pipeline learns imputation and category rules from the training split, which helps avoid information leaking from the validation data.
- `max_iter`, `learning_rate`, `max_leaf_nodes`, and `l2_regularization` control the size and learning speed of the boosting model. `random_state=42` makes its fit repeatable.

## 6. Train and measure RMSE

- `np.log1p(y_train)` transforms skewed prices before fitting. House prices have a long upper tail, and log training reduces the influence of a few very expensive listings.
- `model.predict(X_valid)` predicts in log-price space; `np.expm1` converts the values back to price units.
- `np.maximum(..., 0)` prevents a negative price prediction.
- `mean_squared_error` calculates average squared error. Taking its square root produces RMSE, the hackathon metric. The result is in lakh rupees because that is how the source prices are recorded.
- The model is then fit again on all labeled data. The validation score remains from the untouched holdout, while the final model uses every training row.
- `ARTIFACTS.mkdir(...)` creates the output folder if needed, and `joblib.dump` saves the fitted model for later use.

## 7. Predict and save the submission

- The test CSV is read and passed through the same `add_features` function as training data.
- `test_X` selects the same feature columns as `X`, in the same order.
- The final model predicts test prices; `np.expm1` reverses the log transform and `np.maximum` clips negative results.
- The submission table contains the original test `ID` and predicted `price`, matching the supplied sample's two-column header.
- `to_csv(..., index=False)` writes the file without adding an extra index column.
- `report` records the model name, holdout RMSE, and train/test row counts. `json.dumps(..., indent=2)` makes it readable; `write_text` saves it as `metrics.json`.
- The last three `print` statements show the validation score, training row count, submission path, and column names.

## 8. Start the program

`if __name__ == "__main__":` runs `main()` only when you execute `train.py` directly. If another Python file imports it, training will not start automatically.

Run it from the repository root with:

```powershell
python Python/house_price_prediction/train.py
```

