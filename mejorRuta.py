import networkx as nx

# Definir el grafo que representa el sistema de transporte
viaje = nx.DiGraph()

# Añadir nodos (Municipios)
viaje.add_nodes_from(["Tocancipa", "Zipaquira", "Briceño", "Chia", "Sopo", "Cajica"])

# Añadir aristas (conexiones entre estaciones) con valor (tiempo)
viaje.add_weighted_edges_from([
    ("Tocancipa", "Zipaquira", 40),
    ("Zipaquira", "Tocancipa", 40),  
    ("Tocancipa", "Briceño", 10),
    ("Briceño", "Tocancipa", 10),
    ("Zipaquira", "Chia", 30),
    ("Chia", "Zipaquira", 30),
    ("Briceño", "Chia", 20),
    ("Chia", "Briceño", 20),
    ("Briceño", "Cajica", 20),
    ("Briceño", "Sopo", 10),
    ("Sopo", "Briceño", 10),
    ("Cajica", "Briceño", 20)
])

# Función para encontrar la mejor ruta entre dos puntos
def encontrar_mejor_ruta(grafo, inicio, destino):
    try:
        # Usar el algoritmo de Dijkstra  para encontrar la ruta más corta
        ruta = nx.dijkstra_path(grafo, source=inicio, target=destino, weight='weight')
        costo = nx.dijkstra_path_length(grafo, source=inicio, target=destino, weight='weight')
        return ruta, costo
    except nx.NetworkXNoPath:
        return None, float('inf')

# Punto A y B
punto_inicial = "Sopo"
punto_final = "Cajica"
ruta_optima, costo_total = encontrar_mejor_ruta(viaje, punto_inicial, punto_final)

# Mostrar resultados
if ruta_optima:
    print(f"La mejor ruta desde {punto_inicial} hasta {punto_final} es: {' -> '.join(ruta_optima)}")
    print(f"Tiempo total: {costo_total}")
else:
    print(f"No existe una ruta entre {punto_inicial} y {punto_final}.")
