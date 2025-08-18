import joblib
import pandas as pd

def load_model():
    return joblib.load("models/model.pkl")

def predict_time(distancia, tiempo_base, evento):
    model = load_model()
    df = pd.DataFrame([[distancia, tiempo_base, evento]],
                      columns=["Distancia_km", "Tiempo_base_min", "Evento"])
    return model.predict(df)[0]
