from typing import Dict, List, Tuple
from grafo import Grafo
from queue import PriorityQueue

ColaDePrioridad = PriorityQueue

def dijkstra(grafo: Grafo, origen: str) -> Tuple[Dict[str, int], Dict[str,  str]]:
    distancias = {v: float('inf') for v in grafo}
    padres = {}

    distancias[origen] = 0
    padres[origen] = None
    cola = ColaDePrioridad()

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

def obtener_aristas(grafo: Grafo) -> List[str]:
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes_a(v):
            aristas.append((v, w, grafo.peso_de_arista_entre(v, w)))
    return aristas

def bellman_ford(grafo, origen) -> Tuple[Dict[str, int], Dict[str, str]]:
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


def johnson(grafo: Grafo) -> Tuple[Dict[str, Dict[str, int]], Dict[str, Dict[str, str]]]:
    grafo_BF = Grafo.desde_grafo(grafo)
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