import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from feature_engineering import add_features
from data_preprocessing import load_data, preprocess_data

def evaluate(model_path, test_data_path):
	# Load model
	model = joblib.load(model_path)
	# Load and preprocess test data
	df = load_data(test_data_path)
	df = preprocess_data(df)
	df = add_features(df)
	X_test = df.drop(['demand', 'date'], axis=1)
	y_test = df['demand']
	# Predict
	y_pred = model.predict(X_test)
	# Metrics
	rmse = np.sqrt(mean_squared_error(y_test, y_pred))
	mae = mean_absolute_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	print(f"RMSE: {rmse:.2f}")
	print(f"MAE: {mae:.2f}")
	print(f"R2: {r2:.2f}")

if __name__ == "__main__":
	import sys
	model_path = sys.argv[1] if len(sys.argv) > 1 else "model.joblib"
	test_data_path = sys.argv[2] if len(sys.argv) > 2 else "data/sales.csv"
	evaluate(model_path, test_data_path)
