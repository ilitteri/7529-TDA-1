from grafo import Grafo

def bfs(grafo, s, t):
    visitados = [s]
    vertices = [(s, [s])] # Vertice actual, camino actual
    while vertices:
        vertice_actual, camino = vertices.pop(0)
        for v in grafo.adyacentes_a(vertice_actual):
            if v in visitados or v in camino:
                continue
            if grafo.peso_de_arista_entre(vertice_actual, v) <= 0:
                continue
            visitados.append(v)
            if v == t:
                return camino + [v]
            else:
                vertices.append((v, camino + [v]))
    
    return None   

def aumentar_flujo(grafo, camino):
    aristas = []
    for i in range(len(camino) - 1):
        aristas.append((camino[i],camino[i+1]))

    bottleneck = min([grafo.peso_de_arista_entre(u,v) for u, v in aristas])
    for u,v in aristas:
        flujo_aumentado = grafo.peso_de_arista_entre(u,v) - bottleneck
        grafo.actualizar_peso(u, v, flujo_aumentado)
        if not grafo.estan_unidos(v, u):
            grafo.agregar_arista(v, u, 0)
        flujo_aumentado = grafo.peso_de_arista_entre(v,u) + bottleneck
        grafo.actualizar_peso(v, u, flujo_aumentado)

    return (grafo, bottleneck)

def edmonds_karp(grafo, s, t):
    grafo_residual = Grafo.desde_grafo(grafo)
    camino = bfs(grafo_residual, s, t)
    flujo_maximo = 0
    while camino:
        grafo_residual, bottleneck = aumentar_flujo(grafo_residual, camino)
        flujo_maximo += bottleneck
        camino = bfs(grafo_residual, s, t)
    return (grafo_residual, flujo_maximo)

def corte_minimo(grafo, grafo_residual, source):
    grupo_s = grafo_residual.accesibles_desde(source)
    publicidades = []
    for nodo in grupo_s:
        for nodo_vecino in grafo.adyacentes_a(nodo):
            if nodo_vecino not in grupo_s:
                publicidades.append((nodo, nodo_vecino))
    return publicidades
