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

# 📁 Project Structure

heart-disease-fastapi/
├── app/
│   ├── main.py           # FastAPI app (endpoints)
│   └── schemas.py        # Pydantic input/output models
├── model/
│   └── train_model.py    # Trains RandomForest, saves heart_model.joblib
├── data/
│   └── heart.csv         # Kaggle dataset
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation



## Installation

### Prerequisites
- Python 3.8+
- pip

### Local Setup

1. **Clone the repository**:

git clone https://github.com/MdIftiabMahmudNabil/heart-disease-fastapi.git
cd heart-disease-fastapi

2. **Create virtual environment** (recommended):
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install dependencies**:
pip install -r requirements.txt

## Usage

### Running Locally

Start the FastAPI server:

uvicorn main:app --reload

The API will be available at `http://127.0.0.1:8000`

### API Documentation

Once running, visit:
- **Interactive API docs**: `http://127.0.0.1:8000/docs`
- **Alternative docs**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### 1. Health Check
GET /health

**Response**:
{
"status": "healthy"
}

### 2. API Information
GET /info

**Response**:
{
"name": "Heart Disease Prediction API",
"version": "1.0.0",
"model": "RandomForest",
"description": "Predicts heart disease based on medical indicators"
}


### 3. Heart Disease Prediction
POST /predict

**Request Body**:
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

**Response**:

{
"heart_disease": true
}

### Feature Descriptions

| Feature | Description | Values |
|---------|-------------|---------|
| `age` | Age in years | Integer |
| `sex` | Gender | 1 = male, 0 = female |
| `cp` | Chest pain type | 0-3 |
| `trestbps` | Resting blood pressure | mm Hg |
| `chol` | Serum cholesterol | mg/dl |
| `fbs` | Fasting blood sugar > 120 mg/dl | 1 = true, 0 = false |
| `restecg` | Resting ECG results | 0-2 |
| `thalach` | Maximum heart rate achieved | Integer |
| `exang` | Exercise induced angina | 1 = yes, 0 = no |
| `oldpeak` | ST depression | Float |
| `slope` | Slope of peak exercise ST segment | 0-2 |
| `ca` | Number of major vessels | 0-3 |
| `thal` | Thalassemia | 1-3 |

## Docker Deployment

### Build Docker Image
docker build -t heart-disease-fastapi .

### Run Docker Container
docker run -d -p 8000:8000 heart-disease-fastapi

### Using Docker Compose (if available)
docker-compose up -d


## Cloud Deployment

This application is configured for deployment on cloud platforms:

### Render Deployment
1. Connect your GitHub repository to Render
2. Choose "Web Service"
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Other Platforms
The Docker container can be deployed to:
- Heroku
- AWS ECS
- Google Cloud Run
- Azure Container Instances

## Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Kaggle Heart Disease Dataset
- **Features**: 13 medical indicators
- **Output**: Binary classification (heart disease: true/false)
- **Model File**: `model/heart_model.joblib`

## Development

### Adding New Features
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Testing

Install test dependencies
pip install pytest httpx

Run tests
pytest


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Kaggle Heart Disease Dataset
- FastAPI framework
- scikit-learn library

## Contact

**Author**: Md Iftiab Mahmud Nabil  
**Repository**: [heart-disease-fastapi](https://github.com/MdIftiabMahmudNabil/heart-disease-fastapi)

---

⚠️ **Disclaimer**: This tool is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

