from __future__ import annotations\

from typing import Iterator, Any

class Grafo:
	'''Estructura grafo'''
	def __init__(self, es_dirigido: bool = False, vertices_iniciales: list = []) -> None:
		self.__vertices = {}
		for v in vertices_iniciales:
			self.__vertices[v] = {}
		self.__es_dirigido = es_dirigido

	def __contains__(self, v: str) -> bool:
		return v in self.__vertices

	def __len__(self) -> int:
		return len(self.__vertices)

	def __iter__(self) -> Iterator:
		return iter(self.__vertices)

	@classmethod
	def desde_txt(self, ruta_de_txt: str, es_dirigido: bool=False) -> Grafo:
		grafo = Grafo(es_dirigido)
		with open(ruta_de_txt, 'r') as file:
			lines = file.readlines()
			for line in lines:
				if es_dirigido:
					origen, destino, peso = line.split(',')
					grafo.agregar_vertice(origen)
					grafo.agregar_vertice(destino)
					grafo.agregar_arista(origen, destino, int(peso))
		return grafo

	@classmethod
	def desde_grafo(self, grafo: Grafo) -> Grafo:
		nuevo_grafo = Grafo(grafo.es_dirigido())
		for v in grafo:
			nuevo_grafo.agregar_vertice(v)
		for v in grafo:
			for w in grafo.adyacentes_a(v):
				nuevo_grafo.agregar_arista(v, w, grafo.peso_de_arista_entre(v, w))
		return nuevo_grafo

	def agregar_vertice(self, v: str) -> None:
		if v in self:
			return
		self.__vertices[v] = {}

	def __validar_vertice(self, v: str) -> None:
		if v not in self:
			raise ValueError(f"No hay un vertice {str(v)} en el grafo")

	def __validate_vertices(self, v: str, w: str) -> None:
		self.__validar_vertice(v)
		self.__validar_vertice(w)

	def borrar_vertice(self, v: str) -> None:
		self.__validar_vertice(v)
		for w in self:
			if v in self.__vertices[w]:
				del self.__vertices[w][v]
		del self.__vertices[v]

	def agregar_arista(self, v: str, w: str, peso: Any = None) -> None:
		self.__validate_vertices(v, w)
		if self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " ya tiene como adyacente al vertice " + str(w))
		
		self.__vertices[v][w] = peso
		if not self.__es_dirigido:
			self.__vertices[w][v] = peso

	def borrar_arista(self, v: str, w: str) -> None:
		self.__validate_vertices(v, w)
		if not self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " no tiene como adyacente al vertice " + str(w))

		del self.__vertices[v][w]
		if not self.__es_dirigido:
			del self.__vertices[w][v]

	def estan_unidos(self, v: str, w: str) -> bool:
		return w in self.__vertices[v]

	def peso_de_arista_entre(self, v: str, w: str) -> Any:
		if not self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " no tiene como adyacente al vertice " + str(w))
		return self.__vertices[v][w]

	def obtener_vertices(self) -> list:
		return list(self.__vertices.keys())

	def vertice_random(self) -> str:
		return self.obtener_vertices()[0]

	def adyacentes_a(self, v: str) -> list:
		self.__validar_vertice(v)
		return list(self.__vertices[v].keys())
	
	def orden(self) -> int:
		return len(self)

	def es_dirigido(self) -> bool:
		return self.__es_dirigido

	def __str__(self) -> str:
		cad = ""
		for v in self:
			cad += v
			for w in self.adyacentes_a(v):
				cad += " -> " + w 
			cad += "\n"
		return cad