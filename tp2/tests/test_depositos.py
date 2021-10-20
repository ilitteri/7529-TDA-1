import pytest
from grafo import Grafo
from algoritmos import bellman_ford, dijkstra, johnson

def test01_archivo_sin_depositos_ni_rutas_genera_un_grafo_vacio():
    ruta_grafo = 'tests/depositos_vacios.txt'

    grafo = Grafo.desde_txt(ruta_grafo, es_dirigido=True)
    
    assert len(grafo) == 0


def test02_se_puede_generar_un_grafo_con_rutas_subencionadas():
    rutas = 'tests/depositos_con_rutas_subvencionadas.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)
    
    for v in grafo:
        for w in grafo.adyacentes_a(v):
            assert grafo.peso_de_arista_entre(v, w) < 0


def test03_se_puede_generar_un_grafo_con_rutas_costosas():
    rutas = 'tests/depositos_con_rutas_costosas.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)
    
    for v in grafo:
        for w in grafo.adyacentes_a(v):
            assert grafo.peso_de_arista_entre(v, w) > 0


def test04_se_puede_generar_un_grafo_con_rutas_costosas_y_subencionadas():
    rutas = 'tests/depositos_con_rutas_costosas_y_subvencionadas.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)
    
    for v in grafo:
        for w in grafo.adyacentes_a(v):
            assert grafo.peso_de_arista_entre(v, w)


def test05_no_puede_haber_ciclos_negativos_entre_rutas():
    rutas = 'tests/depositos_con_ciclos_negativos.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)

    with pytest.raises(ValueError):
        bellman_ford(grafo, 'A')


def test06_bellman_ford_resuelve_grafos_sin_ciclos_negativos():
    rutas = 'tests/depositos_sin_ciclos_negativos.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)
    
    distancias, padres = bellman_ford(grafo, 'A')

    assert distancias['A'] == 0
    assert distancias['B'] == -1
    assert distancias['C'] == 2
    assert distancias['D'] == -2
    assert distancias['E'] == 1
    assert padres['A'] == None
    assert padres['B'] == 'A'
    assert padres['C'] == 'B'
    assert padres['D'] == 'E'
    assert padres['E'] == 'B'
    assert len(distancias) == len(grafo)


def test07_dijkstra_resuelve_grafos_sin_ciclos_negativos():
    rutas = 'tests/depositos_sin_ciclos_negativos.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)
    
    distancias, padres = dijkstra(grafo, 'A')

    assert distancias['A'] == 0
    assert distancias['B'] == -1
    assert distancias['C'] == 2
    assert distancias['D'] == -2
    assert distancias['E'] == 1
    assert padres['A'] == None
    assert padres['B'] == 'A'
    assert padres['C'] == 'B'
    assert padres['D'] == 'E'
    assert padres['E'] == 'B'

def test08_johnson_resuelve_el_ejemplo():
    rutas = 'tests/depositos_sin_ciclos_negativos.txt'

    grafo = Grafo.desde_txt(rutas, es_dirigido=True)

    distancias, padres = johnson(grafo) 

    assert distancias['A']['A'] == 0
    assert distancias['A']['B'] == -1
    assert distancias['A']['C'] == 2
    assert distancias['A']['D'] == -2
    assert distancias['A']['E'] == 1
    assert distancias['B']['A'] == float('inf')
    assert distancias['B']['B'] == 0
    assert distancias['B']['C'] == 3
    assert distancias['B']['D'] == -1
    assert distancias['B']['E'] == 2
    assert distancias['C']['A'] == float('inf')
    assert distancias['C']['B'] == float('inf')
    assert distancias['C']['C'] == 0
    assert distancias['C']['D'] == float('inf')
    assert distancias['C']['E'] == float('inf')
    assert distancias['D']['A'] == float('inf')
    assert distancias['D']['B'] == 1
    assert distancias['D']['C'] == 4
    assert distancias['D']['D'] == 0
    assert distancias['D']['E'] == 3
    assert distancias['E']['A'] == float('inf')
    assert distancias['E']['B'] == -2
    assert distancias['E']['C'] == 1
    assert distancias['E']['D'] == -3
    assert distancias['E']['E'] == 0

    assert padres['A']['B'] == 'A'
    assert padres['A']['C'] == 'B'
    assert padres['A']['D'] == 'E'
    assert padres['A']['E'] == 'B'
    assert padres['B']['C'] == 'B'
    assert padres['B']['D'] == 'E'
    assert padres['B']['E'] == 'B'
    assert padres['D']['B'] == 'D'
    assert padres['D']['C'] == 'B'
    assert padres['D']['E'] == 'B'
    assert padres['E']['B'] == 'D'
    assert padres['E']['C'] == 'B'
    assert padres['E']['D'] == 'E'
    with pytest.raises(KeyError):
        padres['E']['A']
        padres['B']['A']
        padres['C']['A']
        padres['C']['B']
        padres['C']['D']
        padres['C']['E']
        padres['D']['A']

    assert len(padres) == len(grafo)
