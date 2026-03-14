import os
import joblib
import numpy as np
from feature_engineering import add_features
from data_preprocessing import load_data, preprocess_data
from train_model import train_model
from evaluate_model import evaluate

def test_model_training_and_prediction():
    # Use a small sample data file
    data_path = "data/sales.csv"
    model_path = "test_model.joblib"
    # Train model
    train_model(data_path, model_path)
    assert os.path.exists(model_path), "Model file was not created."
    # Load model and data
    model = joblib.load(model_path)
    df = load_data(data_path)
    df = preprocess_data(df)
    df = add_features(df)
    X = df.drop(['demand', 'date'], axis=1)
    # Predict
    predictions = model.predict(X)
    assert isinstance(predictions, np.ndarray), "Predictions are not a numpy array."
    assert len(predictions) == len(df), "Number of predictions does not match input."
    print("Test passed: Model training and prediction work as expected.")
    # Clean up
    os.remove(model_path)

if __name__ == "__main__":
    test_model_training_and_prediction()
