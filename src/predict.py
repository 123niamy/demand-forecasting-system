import pandas as pd
import joblib
from feature_engineering import add_features
from data_preprocessing import load_data, preprocess_data

def predict(model_path, input_data_path, output_path=None):
    # Load model
    model = joblib.load(model_path)
    # Load and preprocess new data
    df = load_data(input_data_path)
    df = preprocess_data(df)
    df = add_features(df)
    X = df.drop(['demand', 'date'], axis=1, errors='ignore')
    # Predict
    predictions = model.predict(X)
    df['predicted_demand'] = predictions
    print(df[['date', 'predicted_demand']])
    if output_path:
        df.to_csv(output_path, index=False)
        print(f"Predictions saved to {output_path}")

if __name__ == "__main__":
    import sys
    model_path = sys.argv[1] if len(sys.argv) > 1 else "model.joblib"
    input_data_path = sys.argv[2] if len(sys.argv) > 2 else "data/sales.csv"
    output_path = sys.argv[3] if len(sys.argv) > 3 else None
    predict(model_path, input_data_path, output_path)
