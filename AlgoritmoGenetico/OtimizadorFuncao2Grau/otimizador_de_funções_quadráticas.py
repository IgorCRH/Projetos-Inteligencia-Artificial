# -*- coding: utf-8 -*-
"""Otimizador de Funções Quadráticas.ipynb

Importando as Bibiliotecas
"""

import numpy as np
import random

"""Definindo a Função e Gerando População Inicial"""

def funcaosegundograu(a, b, x, termoindependente):
  if isinstance(x, list):
    return [a*xi**2+b*xi+termoindependente for xi in x]
  else:
    return a*x**2+b*x+termoindependente

def gerarpopulacaoinicial(tamanhopopulacao, valorminimo, valormaximo):
    populacao = [random.randint(valorminimo, valormaximo) for _ in range(tamanhopopulacao)]
    return populacao

"""Calculando o Fitness/Aptidão"""

def calculaaptidao(populacao,a,b,termoindependente):
  valoresaptidao = []

  for individuo in populacao:
    valoresaptidao.append(funcaosegundograu(individuo,a,b,termoindependente))

  return valoresaptidao

"""Procedimento de Seleção pelo Método Roleta"""

def selecaoroleta(populacao,valoresaptidao):
  totalaptidao=sum(valoresaptidao)
  probabilidadedeselecao = [valoraptidao / totalaptidao for valoraptidao in valoresaptidao]
  selecionado = random.choices(populacao,probabilidadedeselecao,k=len(populacao))
  return selecionado

"""Cruzamento/Crossover"""

def cruzamento(pai1, pai2):
    pai1_str = str(pai1)
    pai2_str = str(pai2)
    ponto_de_cruzamento = random.randint(1, min(len(pai1_str), len(pai2_str)))
    filho1 = int(pai1_str[:ponto_de_cruzamento] + pai2_str[ponto_de_cruzamento:])
    filho2 = int(pai2_str[:ponto_de_cruzamento] + pai1_str[ponto_de_cruzamento:])
    return filho1, filho2

"""Mutação"""

def mutacao(populacao, taxamutacao, valorminimo, valormaximo):
  populacaomutacao = []

  for individuo in populacao:
    if random.random() < taxamutacao:
      individuomutado = individuo + random.randint(-1,1)
      individuomutado = max(min(individuomutado,valormaximo),valorminimo)
      populacaomutacao.append(individuomutado)
    else:
      populacaomutacao.append(individuo)
    return populacaomutacao

"""Parâmetros e Interação"""

a = float(input("Digite o coeficiente 'a' (x^2) da função quadrática: "))
b = float(input("Digite o coeficiente 'b' (x) da função quadrática: "))
termoindependente = float(input("Digite o coeficiente 'c' (independente) da função quadrática: "))

minimox = 0
maximox = int(input("Digite o valor máximo de x: "))
tamanhopopulacao = int(input("Digite o tamanho da população: "))
taxamutacao = 0.1
taxadecruzamento = 1.0

populacao = [random.randint(minimox, maximox) for _ in range(tamanhopopulacao)]
geracoes = 50

for geracao in range(geracoes):
  valoresaptidao = calculaaptidao(populacao,a,b,termoindependente)
  populacaoselecionada = selecaoroleta(populacao,valoresaptidao)

  novapopulacao = []

  for i in range(0,len(populacaoselecionada), 2):
    if random.random() < taxadecruzamento:
      filho1, filho2 = cruzamento(populacaoselecionada[i],populacaoselecionada[i+1])
      novapopulacao.append([filho1,filho2])
    else:
      novapopulacao.extend([populacaoselecionada[i],populacaoselecionada[i+1]])

novapopulacaomutada = mutacao(novapopulacao, taxamutacao, minimox, maximox)

populacao = novapopulacao

melhorindividuo = max(populacao, key=lambda x: funcaosegundograu(a, b, x, termoindependente))
melhorfitness = funcaosegundograu(a,b,melhorindividuo,termoindependente)
print(f"Melhor solução encontrada: x = {melhorindividuo}, f(x) = {melhorfitness}")

print("População final:")
for individuo in populacao:
    print(individuo)

