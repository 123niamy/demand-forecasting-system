import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from feature_engineering import add_features
from data_preprocessing import load_data, preprocess_data

def train_model(data_path, model_path):
	# Load and preprocess data
	df = load_data(data_path)
	df = preprocess_data(df)
	df = add_features(df)

	# Define features and target
	X = df.drop(['demand', 'date'], axis=1)
	y = df['demand']

	# Split data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	# Train model
	model = RandomForestRegressor(n_estimators=100, random_state=42)
	model.fit(X_train, y_train)

	# Evaluate
	y_pred = model.predict(X_test)
	rmse = np.sqrt(mean_squared_error(y_test, y_pred))
	print(f"Test RMSE: {rmse:.2f}")

	# Save model
	joblib.dump(model, model_path)
	print(f"Model saved to {model_path}")

if __name__ == "__main__":
	import sys
	data_path = sys.argv[1] if len(sys.argv) > 1 else "data/sales.csv"
	model_path = sys.argv[2] if len(sys.argv) > 2 else "model.joblib"
	train_model(data_path, model_path)
