def dijkstra(grafo, origen) -> tuple(dict, dict):
    distancias = {v: float('inf') for v in grafo}
    padres = {}

    distancias[origen] = 0
    padres[origen] = None
    cola = PriorityQueue()

    for v in grafo:
        cola.put(v)

    while not cola.empty():
        v = cola.get()
        for w in grafo.adyacentes_a(v):
            if distancias[w] > distancias[v] + grafo.peso_de_arista_entre(v, w):
                distancias[w] = distancias[v] + grafo.peso_de_arista_entre(v, w)
                padres[w] = v
                cola.put(w)

    return distancias, padres