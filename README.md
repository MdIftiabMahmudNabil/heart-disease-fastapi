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


## Docker Deployment

### Build Docker Image
```bash
docker build -t heart-disease-fastapi .
```
### Run Docker Container
```bash
docker run -d -p 8000:8000 heart-disease-fastapi
```
### Using Docker Compose
```bash
docker-compose up -d
```
## Cloud Deployment

This project uses a **Dockerfile** at the repo root and a pre-trained model committed to `model/heart_model.joblib`.

### A. Push to GitHub
```bash
git add .
git commit -m "Deploy-ready: Docker + model artifact"
git branch -M main
git remote add origin https://github.com/<your-username>/heart-disease-fastapi.git
git push -u origin main
```
### B) Create a Web Service on Render

1. Go to **Render → New → Web Service**  
2. **Connect** your GitHub repository  
3. **Environment/Language:** Docker *(auto-detected)*  
4. **Branch:** `main`  
5. **Root Directory:** *(leave blank — Dockerfile is at repo root)*  
6. **Instance Type:** **Free** *(sufficient for this demo)*  
7. **Environment Variables:** *none required*  
8. Click **Create Web Service**


### C) Post-create setting

In **Render → Settings → Health Check Path**, set: /health

### D) Verify & Test

1. Watch **Logs** until you see:
```bash
Uvicorn running on http://0.0.0.0:<PORT>
Application startup complete.
```
2. Open your live URL and test:

- `/health` → liveness check  
- `/info` → model info  
- `/docs` → Swagger UI

### Other Platforms
The Docker container can be deployed to:
- **Heroku**
- **AWS ECS**
- **Google Cloud Run**
- **Azure Container Instances**

## Model Information
- **Algorithm:** Random Forest Classifier  
- **Training Data:** Kaggle Heart Disease Dataset (`data/heart.csv`)  
- **Features:** 13 medical indicators  
- **Output:** Binary classification (`heart_disease: true/false`)  
- **Model File:** `model/heart_model.joblib`
## Development

### Adding New Features
1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Add tests if applicable  
5. Submit a pull request

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.  
For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Kaggle Heart Disease Dataset  
- FastAPI framework  
- scikit-learn library

## Contact
**Author:** Md Iftiab Mahmud Nabil  
**Repository:** [heart-disease-fastapi](https://github.com/MdIftiabMahmudNabil/heart-disease-fastapi)

---

> ⚠️ **Disclaimer:** This tool is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

