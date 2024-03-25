# -*- coding: utf-8 -*-
"""caminhocidades.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u7vQZ7kkVFtms19uALuX12RPm1NKFflu

Importando a Bibilioteca
"""

import heapq

"""Definindo a Classe Grafo"""

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        self.vertices[vertice.nome] = vertice

    def adicionar_aresta(self, origem, destino, distancia):
        self.vertices[origem].adicionar_vizinho(destino, distancia)
        self.vertices[destino].adicionar_vizinho(origem, distancia)

"""Definindo a Classe Vértice"""

class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos[vizinho] = distancia

"""Definindo a Classe Estado"""

class Estado:
    def __init__(self, cidade, custo_acumulado, estimativa):
        self.cidade = cidade
        self.custo_acumulado = custo_acumulado
        self.estimativa = estimativa

    def __lt__(self, outro):
        return (self.custo_acumulado + self.estimativa) < (outro.custo_acumulado + outro.estimativa)

"""Percorrendo o Caminho"""

def a_estrela(grafo, inicio, objetivo):
    abertos = []
    heapq.heappush(abertos, inicio)
    visitados = set()

    while abertos:
        estado_atual = heapq.heappop(abertos)

        if estado_atual.cidade == objetivo:
            return estado_atual.custo_acumulado

        if estado_atual.cidade not in visitados:
            visitados.add(estado_atual.cidade)

            for vizinho, distancia in grafo.vertices[estado_atual.cidade].vizinhos.items():
                novo_custo_acumulado = estado_atual.custo_acumulado + distancia
                estimar = estimativa(vizinho, objetivo)
                novo_estado = Estado(vizinho, novo_custo_acumulado, estimar)
                heapq.heappush(abertos, novo_estado)

    return float('inf')

"""Estimativa de Distância das Cidades"""

def estimativa(cidade,objetivo):
  estimativas = {
        'Arad': 366,
        'Bucareste': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 100,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
  }
  return estimativas[cidade]

"""Adicionando os Vértices e Arestas"""

if __name__ == "__main__":
    grafo = Grafo()

grafo.adicionar_vertice(Vertice('Arad'))
grafo.adicionar_vertice(Vertice('Bucareste'))
grafo.adicionar_vertice(Vertice('Craiova'))
grafo.adicionar_vertice(Vertice('Dobreta'))
grafo.adicionar_vertice(Vertice('Eforie'))
grafo.adicionar_vertice(Vertice('Fagaras'))
grafo.adicionar_vertice(Vertice('Giurgiu'))
grafo.adicionar_vertice(Vertice('Hirsova'))
grafo.adicionar_vertice(Vertice('Iasi'))
grafo.adicionar_vertice(Vertice('Lugoj'))
grafo.adicionar_vertice(Vertice('Mehadia'))
grafo.adicionar_vertice(Vertice('Neamt'))
grafo.adicionar_vertice(Vertice('Oradea'))
grafo.adicionar_vertice(Vertice('Pitesti'))
grafo.adicionar_vertice(Vertice('Rimnicu Vilcea'))
grafo.adicionar_vertice(Vertice('Sibiu'))
grafo.adicionar_vertice(Vertice('Timisoara'))
grafo.adicionar_vertice(Vertice('Urziceni'))
grafo.adicionar_vertice(Vertice('Vaslui'))
grafo.adicionar_vertice(Vertice('Zerind'))

grafo.adicionar_aresta('Arad', 'Zerind', 75)
grafo.adicionar_aresta('Arad', 'Timisoara', 118)
grafo.adicionar_aresta('Zerind', 'Oradea', 71)
grafo.adicionar_aresta('Timisoara', 'Lugoj', 111)
grafo.adicionar_aresta('Oradea', 'Sibiu', 151)
grafo.adicionar_aresta('Lugoj', 'Mehadia', 70)
grafo.adicionar_aresta('Mehadia', 'Dobreta', 75)
grafo.adicionar_aresta('Dobreta', 'Craiova', 120)
grafo.adicionar_aresta('Sibiu', 'Rimnicu Vilcea', 80)
grafo.adicionar_aresta('Sibiu', 'Fagaras', 99)
grafo.adicionar_aresta('Rimnicu Vilcea', 'Pitesti', 97)
grafo.adicionar_aresta('Rimnicu Vilcea', 'Craiova', 146)
grafo.adicionar_aresta('Craiova', 'Pitesti', 138)
grafo.adicionar_aresta('Pitesti', 'Bucareste', 101)
grafo.adicionar_aresta('Fagaras', 'Bucareste', 211)
grafo.adicionar_aresta('Bucareste', 'Giurgiu', 90)
grafo.adicionar_aresta('Bucareste', 'Urziceni', 85)
grafo.adicionar_aresta('Urziceni', 'Vaslui', 142)
grafo.adicionar_aresta('Urziceni', 'Hirsova', 98)
grafo.adicionar_aresta('Vaslui', 'Iasi', 92)
grafo.adicionar_aresta('Iasi', 'Neamt', 87)
grafo.adicionar_aresta('Hirsova', 'Eforie', 86)

inicio = Estado('Arad', 0, estimativa('Arad', 'Bucareste'))
objetivo = 'Bucareste'

custo_otimo = a_estrela(grafo, inicio, objetivo)

print("O menor custo ótimo para chegar a Bucareste é:", custo_otimo)

