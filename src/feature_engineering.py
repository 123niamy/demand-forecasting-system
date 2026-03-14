import pandas as pd

def add_features(df):
	"""Add time-based and external features for demand forecasting."""
	df = df.copy()
	print("[add_features] Columns at entry:", df.columns.tolist())
	if 'date' not in df.columns:
		raise KeyError(f"'date' column not found in DataFrame. Columns present: {df.columns.tolist()}")
	# Convert date to datetime
	df['date'] = pd.to_datetime(df['date'])
	# Example time features
	df['day_of_week'] = df['date'].dt.dayofweek
	df['month'] = df['date'].dt.month
	# Lag feature (previous day's demand)
	df['lag_1'] = df['demand'].shift(1).fillna(0)
	# Rolling mean demand (last 3 days)
	df['rolling_mean_3'] = df['demand'].rolling(window=3).mean().fillna(0)
	return df
