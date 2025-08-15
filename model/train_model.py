import os
import glob
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

MODEL_OUT = os.getenv("MODEL_PATH", "model/heart_model.joblib")

def load_heart_csv():
    try:
        import kagglehub
        path = kagglehub.dataset_download("johnsmith88/heart-disease-dataset")
        csvs = glob.glob(os.path.join(path, "**", "heart.csv"), recursive=True)
        if csvs:
            print(f"Loaded via kagglehub: {csvs[0]}")
            return pd.read_csv(csvs[0])
    except Exception as e:
        print("kagglehub failed or unavailable:", e)

    fallback = glob.glob(os.path.join("model", "*heart*.csv"))
    if fallback:
        print(f"Loaded local CSV: {fallback[0]}")
        return pd.read_csv(fallback[0])

    raise FileNotFoundError("Could not load heart.csv via kagglehub or local model/ folder.")

def main():
    df = load_heart_csv()

    expected = ["age","sex","cp","trestbps","chol","fbs","restecg",
                "thalach","exang","oldpeak","slope","ca","thal","target"]
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset missing columns: {missing}. Found: {list(df.columns)}")

    X = df[expected[:-1]].copy()
    y = df["target"].astype(int)

    for c in X.columns:
        X[c] = pd.to_numeric(X[c], errors="coerce")
    X = X.fillna(X.median(numeric_only=True))

    pipe = Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    pipe.fit(X_train, y_train)

    acc = pipe.score(X_test, y_test)
    print(f"Validation accuracy: {acc:.3f} (accuracy is not the focus here)")

    os.makedirs(os.path.dirname(MODEL_OUT), exist_ok=True)
    joblib.dump(pipe, MODEL_OUT)
    print(f"Saved model to {MODEL_OUT}")

if __name__ == "__main__":
    main()
