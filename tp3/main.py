from grafo import Grafo
from edmonds_karp import edmonds_karp, corte_minimo

def main():
    grafo, a, b = Grafo.desde_txt("ejemplo.txt", es_dirigido=True)
    (grafo_residual, flow) = edmonds_karp(grafo, a, b)
    print(f"El flujo maximo es: {flow}")
    publicidades = corte_minimo(grafo, grafo_residual, "A")
    print(f"Las publicidades deben colocarse en las siguientes aristas: {publicidades}")

main()