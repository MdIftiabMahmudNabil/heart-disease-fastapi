Heart Disease Prediction API
A FastAPI-based service for predicting heart disease using machine learning, containerized with Docker, and deployable to Render. This project prioritizes Dockerization and deployment over maximum model accuracy.
Features

FastAPI Backend: Provides a RESTful API for heart disease prediction.
Machine Learning: Uses a pre-trained model to predict heart disease risk based on clinical data.
Dockerized: Containerized for consistent deployment across environments.
Render Deployment: Easily deployable to Render for scalable hosting.
Swagger UI: Interactive API documentation at /docs.

Project Structure
heart-disease-fastapi/
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── schemas.py         # Pydantic models for request validation
│   └── model/
│       └── heart_model.joblib  # Pre-trained ML model
├── Dockerfile             # Docker build instructions
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file

Prerequisites

Python 3.10+
Docker (for containerization)
pip (Python package installer)
Render account (for deployment)

Installation

Clone the Repository:
git clone https://github.com/MdIftiabMahmudNabil/heart-disease-fastapi.git
cd heart-disease-fastapi


Create and Activate a Virtual Environment:
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate


Install Dependencies:
pip install -r requirements.txt



Running Locally

Start the FastAPI Server:
uvicorn app.main:app --host 0.0.0.0 --port 8000


Access the Application:

Web Interface: http://localhost:8000
API Documentation: http://localhost:8000/docs



Running with Docker

Build the Docker Image:
docker build -t heart-disease-fastapi .


Run the Docker Container:
docker run -p 8000:8000 heart-disease-fastapi


Access the Application:

Web Interface: http://localhost:8000
API Documentation: http://localhost:8000/docs



Deploying to Render

Push the repository to GitHub.
Create a new Web Service on Render.
Select Docker as the environment.
Connect your GitHub repository (MdIftiabMahmudNabil/heart-disease-fastapi).
Deploy and test the live API at the provided Render URL (/docs for Swagger UI).

API Endpoints

GET /health: Check the API's health status.
POST /predict: Submit clinical data for heart disease prediction.
Request Body: JSON with features (e.g., age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal).
Response: Prediction result (0 = no heart disease, 1 = heart disease).



Dataset
The model is trained on the Kaggle Heart Disease Dataset, focusing on binary classification (0 = no heart disease, 1 = heart disease).
Notes

Ensure the heart_model.joblib file is present in the app/model/ directory.
Clinical data inputs should use standard units.
The project focuses on Dockerization and deployment, not optimizing model accuracy.

Troubleshooting

Application Won't Start:
Verify Python version (3.10+).
Ensure all dependencies are installed (pip install -r requirements.txt).
Check for the presence of heart_model.joblib.


Prediction Errors:
Validate input data ranges and formats.
Ensure all required features are provided in the /predict request.



Contributing
Contributions are welcome! Please:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

License
This project is licensed under the MIT License.
