import networkx as nx
from graph.graph import build_graph

def shortest_path(origen, destino):
    G = build_graph()
    path = nx.shortest_path(G, source=origen, target=destino, weight="tiempo_predicho")
    tiempo = nx.shortest_path_length(G, source=origen, target=destino, weight="tiempo_predicho")
    distancia = sum(
        G[u][v]["distancia"] for u, v in zip(path[:-1], path[1:])
    )
    return path, tiempo, distancia

