# Bengaluru House Price Prediction

This project trains a regression model from the Bengaluru house listings in `train_(2)_(1)_(1)_(1).csv` at the repository root. The target is the source dataset's `price` column, expressed in lakh rupees.

## Feature engineering

- Converts `total_sqft` ranges to their midpoint and converts common area units to square feet.
- Extracts the bedroom count from values such as `2 BHK`, `4 Bedroom`, and `1 RK`.
- Creates `sqft_per_bhk` and `bath_per_bhk` ratios, plus a ready-to-move flag.
- Normalizes area type and locality text, and reduces rare locality categories during one-hot encoding.
- Imputes missing numeric values and encodes categories inside a scikit-learn pipeline, fitted only on the training split.
- Drops `ID` because it identifies a row, and `society` because it is highly incomplete and high-cardinality.

The beginner version uses Histogram Gradient Boosting, which had the best holdout RMSE in the earlier model comparison. It predicts log price during training, then converts predictions back to the source price scale. The holdout set is 20% of the usable listings, selected with a fixed random seed. After measuring RMSE, the model is refit on all usable training rows.

## Run

From the repository root:

```powershell
python -m pip install -r Python/house_price_prediction/requirements.txt
python Python/house_price_prediction/train.py
```

The script expects the test CSV in your Downloads folder. If yours is elsewhere, change `TEST_FILE` near the top of `train.py`. The run saves `bengaluru_house_price.joblib` and `metrics.json` under `Python/house_price_prediction/artifacts/`, and writes `submission.csv` at the repository root. The submission matches the sample header exactly: `ID` and `price`, with one row for each test listing.

See [`CODE_WALKTHROUGH.md`](CODE_WALKTHROUGH.md) for a beginner-focused explanation of the script.

## Dataset

The training file is available in the repository as [`train_(2)_(1)_(1)_(1).csv`](https://github.com/kiranitmca/PES-MTECH/blob/main/train_%282%29_%281%29_%281%29_%281%29.csv). The test and sample-submission CSVs used for this run are in the user's Downloads folder.

