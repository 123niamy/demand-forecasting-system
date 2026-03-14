from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
from src.feature_engineering import add_features
from src.data_preprocessing import preprocess_data
import io

app = FastAPI()

# Load model at startup
model = joblib.load("model.joblib")

@app.post("/predict/")
def predict(file: UploadFile = File(...)):
    # Read uploaded CSV file
    contents = file.file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df = preprocess_data(df)
    df = add_features(df)
    X = df.drop(['demand', 'date'], axis=1, errors='ignore')
    predictions = model.predict(X)
    df['predicted_demand'] = predictions
    # Return predictions as JSON
    return df[['date', 'predicted_demand']].to_dict(orient='records')

# To run: uvicorn src.api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api:app", host="127.0.0.1", port=8000, reload=True)
