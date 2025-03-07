# 🚀 ML Workflow & CI/CD Pipeline for Wine Quality Prediction

## 📌 Overview
This repository demonstrates a complete **Machine Learning Workflow** integrated with **MLflow for experiment tracking** and **CI/CD pipelines** for model deployment. The project uses the **Wine Quality dataset** and implements multiple ML algorithms including:
- **Random Forest** 🌲
- **XGBoost** ⚡
- **LightGBM** 🌞
- **Support Vector Machine (SVM)** 🔄
- **Linear Regression** ➕

## 📂 Project Structure
```
├── data/                 # Dataset files (Wine Quality dataset)
├── notebooks/            # Jupyter notebooks for EDA and model training
├── src/
│   ├── data_processing.py # Data cleaning and preprocessing
│   ├── train.py           # Model training script
│   ├── evaluate.py        # Model evaluation
│   ├── inference.py       # Model inference script
├── models/               # Trained model artifacts
├── mlruns/               # MLflow experiment tracking
├── Dockerfile            # Docker setup for deployment
├── requirements.txt      # Dependencies
├── .github/workflows/    # GitHub Actions for CI/CD
├── README.md             # Project documentation
```

## 📊 ML Workflow
### 1️⃣ Data Preprocessing
- Missing value handling
- Feature scaling
- Train-test split

### 2️⃣ Model Training & Experiment Tracking
- MLflow is used to log model performance metrics.
- Hyperparameter tuning is conducted for optimal results.

### 3️⃣ Model Evaluation
- Models are compared using RMSE, MAE, and R² scores.

### 4️⃣ Model Deployment & CI/CD Pipeline
- **GitHub Actions** for automatic testing, training, and deployment.
- **Docker** for containerizing the ML model.
- **Kubernetes (Optional)** for scalable deployment.

## 🚀 Getting Started
### 🔹 Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Git
- Docker (for deployment)
- MLflow

### 🔹 Installation
```bash
git clone https://github.com/your-repo/mlops-wine-quality.git
cd mlops-wine-quality
pip install -r requirements.txt
```

### 🔹 Running the ML Pipeline
1. **Run data preprocessing:**
   ```bash
   python src/data_processing.py
   ```
2. **Train the model and track experiments with MLflow:**
   ```bash
   python src/train.py
   ```
3. **Evaluate the model:**
   ```bash
   python src/evaluate.py
   ```
4. **Deploy the model using Docker:**
   ```bash
   docker build -t wine_quality_model .
   docker run -p 5000:5000 wine_quality_model
   ```

## 🤖 CI/CD Pipeline (GitHub Actions)
The repository includes a **GitHub Actions** workflow for:
- **Continuous Integration (CI):** Linting, unit tests, and model validation.
- **Continuous Deployment (CD):** Deploying the trained model as an API.

### Workflow Structure
```yaml
name: ML Pipeline CI/CD

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Train Model
        run: python src/train.py
```

## 📈 MLflow Experiment Tracking
Launch MLflow UI to track experiments:
```bash
mlflow ui
```
Then, open `http://localhost:5000` in your browser.

## 📜 License
This project is licensed under the **MIT License**.

## 💡 Future Enhancements
- Integrate **Evidently AI** for model monitoring.
- Add **AWS/GCP/Azure deployment** for cloud-based serving.
- Automate **data drift detection** and retraining.

🚀 Happy Coding! Feel free to contribute and raise PRs!

