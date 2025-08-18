from graph.shortest_path import shortest_path

if __name__ == "__main__":
    origen = "Tunja"
    destino = "Manizales"
    path, tiempo, distancia = shortest_path(origen, destino)
    print(f"Ruta más corta de {origen} a {destino}: {path}")
    print(f"Distancia total: {distancia:.2f} km")
    print(f"Tiempo estimado: {tiempo:.2f} minutos")
