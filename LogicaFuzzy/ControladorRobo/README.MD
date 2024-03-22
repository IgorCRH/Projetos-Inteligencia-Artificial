## Descrição
Projeto para desenvolver um sistema fuzzy para um controlador de um robô, com as seguintes proposições:

## Enunciado do Problema
O objetivo do exercício é desenvolver um controlador para um robô seguidor de linha
utilizando lógica fuzzy.
Os requisitos do controlador fuzzy são os seguintes:
- Utilizar três sensores de entrada (esquerda, centro e direita).
- Para cada sensor elaborar um conjunto fuzzy com três variáveis linguísticas.
- Compor um conjunto de saída com 5 variáveis linguisticas
- Compor as 27 regras resultantes destes conjuntos de modo a manter o robô sobre a
linha
- Calcular o valor de disparo de cada regra.
- Compor os valores de cada conjunto de saída pelo máximo.
- Determinar o valor de saída pela média ponderada dos máximos.
- Determinar a velocidade de direção de rotação de cada roda com base no valor de saída. 

## Bibiliotecas Utilizadas

- NumPy
- Matplotlib
- Scikit-Fuzzy
