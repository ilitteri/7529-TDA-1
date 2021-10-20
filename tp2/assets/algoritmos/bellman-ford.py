def obtener_aristas(grafo) -> list:
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes_a(v):
            aristas.append((v, w, grafo.peso_de_arista_entre(v, w)))
    return aristas

def bellman_ford(grafo, origen) -> tuple(dict(str, dict), dict(str, dict)):
    distancias = {}
    padres = {}
    for v in grafo:
        distancias[v] = float('inf')

    distancias[origen] = 0
    padres[origen] = None
    aristas = obtener_aristas(grafo)
    for _ in range(len(grafo) - 1):
        for v, w, peso in aristas:
            if distancias[v] + peso < distancias[w]:
                distancias[w] = distancias[v] + peso
                padres[w] = v
        
    for v, w, peso in aristas:
        if distancias[v] + peso < distancias[w]:
            raise ValueError('El grafo tiene ciclos negativos')

    return distancias, padres