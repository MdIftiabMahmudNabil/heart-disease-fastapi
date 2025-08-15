# Heart Disease Prediction API with FastAPI

A lightweight FastAPI service that predicts heart disease using a scikit-learn RandomForest trained on the Kaggle Heart Disease dataset (data/heart.csv). The saved model (model/heart_model.joblib) powers three endpoints: GET /health, GET /info, and POST /predict, returning heart_disease: true|false. Containerized with Docker and deployed on Render.

## Features

- **Machine Learning Model**: RandomForest classifier trained with scikit-learn
- **Fast API Framework**: High-performance, easy-to-use web framework
- **Three API Endpoints**:
  - `GET /health`: Health check endpoint
  - `GET /info`: Provides basic information about the API
  - `POST /predict`: Heart disease prediction endpoint
- **Docker Support**: Fully containerized for easy deployment
- **Cloud Ready**: Deployable to Render and other cloud platforms

## 📁 Project Structure

```text
heart-disease-fastapi/
├── app/
│   ├── main.py              # FastAPI app (endpoints)
│   └── schemas.py           # Pydantic input/output models
├── model/
│   └── train_model.py       # Trains RandomForest, saves heart_model.joblib
├── data/
│   └── heart.csv            # Kaggle dataset (you provide this locally)
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```
## Installation

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/MdIftiabMahmudNabil/heart-disease-fastapi.git
cd heart-disease-fastapi
```
2. **Create virtual environment**

**macOS / Linux**
```bash
python -m venv venv
source venv/bin/activate
```
**Windows**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
## Usage

### Running Locally
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

### API Documentation

Once running, visit:

- **Interactive API docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative docs (ReDoc):** http://127.0.0.1:8000/redoc

## API Endpoints

### 1. Health Check
**GET** `/health`

**Response**
```json
{
  "status": "healthy"
}
```

### 2. API Information
**GET** `/info`

**Response**
```json
{
  "name": "Heart Disease Prediction API",
  "version": "1.0.0",
  "model": "RandomForest",
  "description": "Predicts heart disease based on medical indicators"
}
```

### 3. Heart Disease Prediction
**POST** `/predict`

**Request Body**
```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```
**Response**
```json
{
  "heart_disease": true
}
```
### Feature Descriptions

| Feature    | Description                               | Values                 |
|------------|-------------------------------------------|------------------------|
| `age`      | Age in years                               | Integer                |
| `sex`      | Gender                                     | 1 = male, 0 = female   |
| `cp`       | Chest pain type                            | 0–3                    |
| `trestbps` | Resting blood pressure                     | mm Hg                  |
| `chol`     | Serum cholesterol                          | mg/dl                  |
| `fbs`      | Fasting blood sugar > 120 mg/dl            | 1 = true, 0 = false    |
| `restecg`  | Resting ECG results                        | 0–2                    |
| `thalach`  | Maximum heart rate achieved                | Integer                |
| `exang`    | Exercise induced angina                    | 1 = yes, 0 = no        |
| `oldpeak`  | ST depression                              | Float                  |
| `slope`    | Slope of peak exercise ST segment          | 0–2                    |
| `ca`       | Number of major vessels                    | 0–3                    |
| `thal`     | Thalassemia                                | 1–3                    |
