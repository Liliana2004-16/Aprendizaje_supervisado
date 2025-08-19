from typing import List, Dict, Tuple
from expert.knowledge_base import EVENT_MESSAGES, normalize_event

def summarize_path(path: List[str],
                   edges: List[Tuple[str, str, Dict]]) -> Dict:
    total_dist = sum(e[2].get("distancia", 0.0) for e in edges)
    total_time = sum(e[2].get("tiempo_predicho", 0.0) for e in edges)

    issues = []
    for u, v, data in edges:
        evt = normalize_event(data.get("evento", "ninguno"))
        if evt != "ninguno":
            issues.append({
                "tramo": f"{u} → {v}",
                "evento": evt,
                "msg": EVENT_MESSAGES.get(evt, "Afectación detectada."),
                "tiempo": data.get("tiempo_predicho", 0.0)
            })

    worst = max(issues, key=lambda x: x["tiempo"], default=None)

    return {
        "ruta": path,
        "distancia_km": total_dist,
        "tiempo_min": total_time,
        "incidencias": issues,
        "tramo_critico": worst
    }

def render_response(summary: Dict, origen: str, destino: str) -> str:
    if not summary["ruta"]:
        return (f"No fue posible encontrar una ruta válida entre {origen} y {destino} "
                "debido a cierres en todas las alternativas.")

    ruta = " → ".join(summary["ruta"])
    km = summary["distancia_km"]
    minutes = summary["tiempo_min"]

    partes = [
        f"Ruta más corta de {origen} a {destino}: {ruta}",
        f"Distancia total: {km:.2f} km",
        f"Tiempo estimado: {minutes:.2f} min",
    ]

    if not summary["incidencias"]:
        partes.append(f"Observación: {EVENT_MESSAGES['ninguno']}")
        return "\n".join(partes)

    partes.append("Incidencias detectadas en la ruta:")
    for i in summary["incidencias"]:
        partes.append(f" - {i['tramo']}: {i['msg']}")

    if summary["tramo_critico"]:
        tc = summary["tramo_critico"]
        partes.append(f"Tramo más crítico: {tc['tramo']} ({tc['msg']})")

    return "\n".join(partes)
