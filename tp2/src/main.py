#!/usr/bin/python3
from __future__ import annotations

import sys
from tabulate import tabulate
from grafo import Grafo
from algoritmos import johnson

def construir_camino(padres: dict, origen: str, destino: str) -> list:
    '''
    Construye un camino a partir de un diccionario de padres.
    '''
    w = origen
    v = destino
    path = []
    if destino not in padres:
        return None
    while v != w:
        path.append(v)
        v = padres[v]
    path.append(w)
    return path[::-1]

def procesar_distancias(distancias: dict) -> list:
    '''Mapea la matriz de distancias de un diccionario de diccionarios a una 
    lista de listas'''
    matriz_resultante = []
    header = list(distancias.keys())
    header.insert(0, "")
    matriz_resultante.append(header)

    for v in distancias:
        fila = list(distancias[v].values())
        fila.insert(0, v)
        matriz_resultante.append(fila)

    return matriz_resultante

def obtener_vertice_con_menor_distancia_total(distancias: list(list)) -> tuple(int, int):
    '''Obtiene el vértice de origen cuya distancia total a los demás vértices es
    la mínima'''
    mejor_nodo: str = ""
    mejor_distancia: float | int = float("inf")

    for fila in distancias[1:]:
        distancia_total = sum(fila[1:])
        if distancia_total < mejor_distancia:
            mejor_nodo = fila[0]
            mejor_distancia = distancia_total

    return mejor_nodo, mejor_distancia

def mostrar_tabla_de_distancias(distancias: list) -> None:
    '''Imprime en pantalla una tabla con las distancias resultantes'''
    distancias_formateadas = tabulate(distancias, tablefmt="fancy_grid")
    print(distancias_formateadas)

def obtener_mejor_alternativa_de_ubicacion_para_fabrica(rutas: Grafo) -> tuple(str, int):
    '''Obtiene la mejor alternativa para ubicar la fábrica a construir'''
    distancias_johnson, _ = johnson(rutas)
    lista_de_distancias = procesar_distancias(distancias_johnson)
    mostrar_tabla_de_distancias(lista_de_distancias)

    return obtener_vertice_con_menor_distancia_total(lista_de_distancias)
    

def main():
    rutas_entre_depositos = Grafo.desde_txt(sys.argv[1], es_dirigido=True)
    deposito, distancia_de_ruta_entre_depositos = obtener_mejor_alternativa_de_ubicacion_para_fabrica(rutas_entre_depositos)
    print(f'La mejor ubicación para ubicar la fábrica es en el depósito "{deposito}", ya que desde allí, recorrer la ruta que lleva a los demás depósitos cuesta "{distancia_de_ruta_entre_depositos}"')

if __name__ == "__main__":
    main()