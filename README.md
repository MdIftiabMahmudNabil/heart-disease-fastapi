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

### Prerequisites
- Python **3.8+**
- `pip`

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
