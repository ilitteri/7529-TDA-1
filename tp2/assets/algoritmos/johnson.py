def johnson(grafo: Graph) -> tuple(dict, dict):
    grafo_BF = Graph.desde_grafo(grafo)
    grafo_BF.agregar_vertice("0")
    for v in grafo_BF:
        grafo_BF.agregar_arista("0", v, 0)

    distancias_BF, _ = bellman_ford(grafo_BF, "0") 

    for u in grafo:
        h_u = distancias_BF[u]
        for v in grafo.adyacentes_a(u):
            h_v = distancias_BF[v]
            w = grafo.peso_de_arista_entre(u, v)
            grafo.borrar_arista(u, v)
            grafo.agregar_arista(u, v, w+h_u-h_v)

    padres_D = {}
    distancias_D = {}
    for v in grafo:
        distancias_D[v], padres_D[v] = dijkstra(grafo, v)
    
    for v in distancias_D:
        for w in distancias_D[v]:
            distancias_D[v][w] = distancias_D[v][w] - distancias_BF[v] + distancias_BF[w]

    return distancias_D, padres_D