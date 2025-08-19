import joblib
import pandas as pd

def load_model():
    return joblib.load("models/model.pkl")

def normalize_evento(evento: str) -> str:
    """Normaliza el nombre del evento para que coincida con el entrenamiento"""
    evento = evento.strip().lower()
    if evento == "sin evento":
        return "ninguno"
    return evento

def predict_time(distancia, tiempo_base, evento):
    model = load_model()
    
   
    evento = normalize_evento(evento)

    df = pd.DataFrame([[distancia, tiempo_base, evento]],
                      columns=["Distancia_km", "Tiempo_base_min", "Evento"])
    
    return model.predict(df)[0]

