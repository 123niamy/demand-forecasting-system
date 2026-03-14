def load_data(filepath):
	"""Load raw sales data from a CSV file."""
	import pandas as pd
	df = pd.read_csv(filepath)
	# Strip whitespace from column names
	df.columns = df.columns.str.strip()
	return df

def preprocess_data(df):
	"""Clean and preprocess the data."""
	# Example: fill missing values
	df = df.fillna(0)
	return df


# Demonstration: Load, preprocess, and add features
if __name__ == "__main__":
	import os
	from feature_engineering import add_features
	data_path = "data/sales.csv"
	abs_path = os.path.abspath(data_path)
	print(f"Loading data from: {abs_path}")
	df = load_data(data_path)
	print("Raw data sample:")
	print(df.head())
	print("Columns after loading:", df.columns.tolist())

	df_clean = preprocess_data(df)
	print("\nAfter preprocessing:")
	print(df_clean.head())
	print("Columns after preprocessing:", df_clean.columns.tolist())

	df_features = add_features(df_clean)
	print("\nAfter feature engineering:")
	print(df_features.head())
