SEVERITY_FACTORS = {
    "ninguno": 1.00,
    "trafico": 2.82,               
    "obra vial": 2.33,
    "accidente de trafico": 1.50,
    "via cerrada": float("inf"),    
}

EVENT_MESSAGES = {
    "ninguno": "Sin afectaciones reportadas.",
    "trafico": "Tráfico intenso: incrementa el tiempo (~2.8x).",
    "obra vial": "Obras viales: posibles demoras (~2.3x).",
    "accidente de trafico": "Accidente reportado: incremento moderado (~1.5x).",
    "via cerrada": "Vía cerrada",
}

def normalize_event(evt: str) -> str:
    return (evt or "").strip().lower()
