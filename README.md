## ⚠️ Challenges Encountered

- **Data Quality & Consistency:** Ensuring the sales data was clean, correctly formatted, and free of missing or inconsistent values required careful preprocessing and validation.
- **Feature Engineering:** Identifying and creating meaningful features (e.g., lagged demand, rolling averages, time-based features) to improve model performance was iterative and required domain understanding.
- **Model Generalization:** Avoiding overfitting with limited data and ensuring the model could generalize to unseen demand patterns was addressed through validation and regularization.
- **Module Import Paths:** Handling Python import errors (especially for API deployment) required adjusting import statements and project structure for compatibility with FastAPI and Uvicorn.
- **API Deployment:** Packaging the model as a robust, user-friendly API involved resolving dependency issues and ensuring smooth file uploads and predictions.
- **Reproducibility:** Maintaining reproducible results across scripts and environments required careful management of random seeds and dependencies.
## 🧠 Topics Covered

- Supervised Machine Learning (Regression)
- Data Preprocessing & Cleaning
- Feature Engineering & Selection
- Model Training & Hyperparameter Tuning
- Model Evaluation (RMSE, MAE, R²)
- Batch & Real-Time Prediction
- REST API Deployment (FastAPI)
- Automated Testing & Reproducibility
## ℹ️ About

This project is a comprehensive, end-to-end machine learning system for demand forecasting in e-commerce. It enables businesses to predict product demand, optimize inventory, and make data-driven decisions. The solution includes data preprocessing, feature engineering, model training and evaluation, automated testing, and a production-ready API for real-time or batch predictions. Designed for clarity, reproducibility, and extensibility, this project is ideal for both practical deployment and as a portfolio showcase for ML engineering skills.
## 🎥 Project Demo

<p align="center">
	<img src="https://raw.githubusercontent.com/123niamy/demand-forecasting-system/main/demo/demo-screenshot.png" alt="Demo Screenshot" width="600"/>
</p>

<!-- Optionally, add a GIF demo -->
<!--
<p align="center">
	<img src="https://raw.githubusercontent.com/123niamy/demand-forecasting-system/main/demo/demo.gif" alt="Demo GIF" width="600"/>
</p>
-->

<!-- Optionally, add a video demo link -->
<!--
**Watch the full demo:** [YouTube Video](https://youtu.be/your-demo-link)
-->
(The file `c:\Users\user\Machine learning project\README.md` exists, but is empty)

<div align="center">
	<h1>Demand Forecasting System for E-Commerce</h1>
	<p><b>End-to-end machine learning solution for predicting product demand, optimizing inventory, and improving business decisions.</b></p>

	<!-- Badges -->
	<p>
		<a href="https://www.python.org/downloads/release/python-3140/"><img src="https://img.shields.io/badge/python-3.14-blue.svg" alt="Python 3.14"></a>
		<a href="https://github.com/123niamy/demand-forecasting-system/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
		<a href="https://github.com/123niamy/demand-forecasting-system/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status"></a>
		<a href="https://github.com/123niamy/demand-forecasting-system/issues"><img src="https://img.shields.io/github/issues/123niamy/demand-forecasting-system.svg" alt="Issues"></a>
	</p>
</div>

---

## 🚀 Overview
This project provides a complete, production-ready pipeline for demand forecasting in e-commerce. It covers data preprocessing, feature engineering, model training, evaluation, automated testing, and API deployment for real-time or batch predictions.

## 🛒 Business Problem
Accurately predict product demand to optimize inventory, reduce stockouts/overstock, and improve cash flow for e-commerce businesses.

## 📊 Data
- Historical sales data: `date`, `product_id`, `demand`, `price`, `promotion`, `holiday`, `economic_index`
- External factors: promotions, holidays, economic indicators

## 🧩 Solution Approach
1. **Data Preprocessing & Feature Engineering**: Clean, transform, and enrich raw data for modeling.
2. **Exploratory Data Analysis (EDA)**: Understand demand patterns and feature relationships.
3. **Model Training**: Train a regression model (Random Forest) to predict demand.
4. **Evaluation**: Assess model performance with RMSE, MAE, and R² metrics.
5. **Prediction & Deployment**: Batch prediction script and FastAPI-based REST API for real-time use.
6. **Testing**: Automated script to validate the pipeline end-to-end.

## 🗂️ Project Structure
```
├── data/                # Raw data files (e.g., sales.csv)
├── notebooks/           # Jupyter notebooks for EDA
├── src/                 # Source code
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│   ├── test_model.py
│   └── api.py           # FastAPI deployment
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/123niamy/demand-forecasting-system.git
cd demand-forecasting-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Data Preprocessing & Feature Engineering
```bash
python src/data_preprocessing.py
```

### 4. Model Training
```bash
python src/train_model.py
```

### 5. Model Evaluation
```bash
python src/evaluate_model.py
```

### 6. Batch Prediction
```bash
python src/predict.py model.joblib data/sales.csv
```

### 7. Automated Testing
```bash
python src/test_model.py
```

### 8. API Deployment (FastAPI)
```bash
uvicorn src.api:app --reload
# Visit http://127.0.0.1:8000/docs to test the API
```

## 📝 Example API Usage
Upload a CSV file to `/predict/` endpoint via Swagger UI or with curl:
```bash
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@data/sales.csv"
```

## 📈 Results
- Example metrics: RMSE, MAE, R² (see evaluation output)
- Model and predictions are reproducible and ready for deployment

## 🤝 Contributing
Pull requests and issues are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License.

---
<div align="center">
	<b>Showcase your ML engineering skills with a real-world, production-ready pipeline!</b>
</div>
