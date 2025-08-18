import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def train():
    # Cargar dataset
    df = pd.read_csv("data/viajes.csv")

    # Variables de entrada y salida
    X = df[["Distancia_km", "Tiempo_base_min", "Evento"]]
    y = df["Tiempo_real_min"]

    # Preprocesamiento: convertir 'Evento' en variables categóricas
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(), ["Evento"])],
        remainder="passthrough"
    )

    # Modelo
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])

    # Entrenar
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    # Guardar modelo entrenado
    joblib.dump(model, "models/model.pkl")
    print(" Modelo entrenado y guardado en models/model.pkl")

if __name__ == "__main__":
    train()
