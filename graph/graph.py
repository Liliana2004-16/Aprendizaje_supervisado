import csv
import pandas as pd
import networkx as nx
from models.predict import predict_time

def build_graph():
    G = nx.Graph()
    with open("data/viajes.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            origen = row["Origen"].strip()
            destino = row["Destino"].strip()
            distancia = float(row["Distancia_km"])
            evento = row["Evento"].strip().lower()
            tiempo_real = float(row["Tiempo_real_min"])

            
            if evento != "vía cerrada":
                G.add_edge(origen, destino, distancia=distancia, tiempo=tiempo_real)
    
    return G

