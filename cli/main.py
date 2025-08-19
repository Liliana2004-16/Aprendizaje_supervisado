import networkx as nx
from graph.graph import build_graph
from expert.response_engine import summarize_path, render_response

def calcular_ruta(origen: str, destino: str):
    G = build_graph()

    try:
        path = nx.shortest_path(G, source=origen, target=destino, weight="tiempo_predicho")

        edges = []
        for u, v in zip(path[:-1], path[1:]):
            data = G.get_edge_data(u, v)
            edges.append((u, v, data))
 
        summary = summarize_path(path, edges)

        return render_response(summary, origen, destino)

    except nx.NetworkXNoPath:
        return f"No existe ruta disponible entre {origen} y {destino}."

if __name__ == "__main__":
    origen = "Tunja"
    destino = "Manizales"
    respuesta = calcular_ruta(origen, destino)
    print(respuesta)
