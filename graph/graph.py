import csv
import networkx as nx
from expert.knowledge_base import SEVERITY_FACTORS, normalize_event
from unidecode import unidecode 

def normalize_city(name: str) -> str:

    return unidecode(name.strip().title())

def build_graph():
    G = nx.Graph()
    with open("data/viajes.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            origen = normalize_city(row["Origen"])
            destino = normalize_city(row["Destino"])
            distancia = float(row["Distancia_km"])
            tiempo_base = float(row["Tiempo_base_min"])
            evento = normalize_event(row["Evento"])

            factor = SEVERITY_FACTORS.get(evento, 1.0)

            if evento == "vía cerrada":
                continue

            tiempo_predicho = tiempo_base * factor

            G.add_edge(
                origen,
                destino,
                distancia=distancia,
                tiempo_base=tiempo_base,
                tiempo_predicho=tiempo_predicho,
                evento=evento
            )
    return G

