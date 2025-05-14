🔧 Sistema de Localização e Compra de Peças Automotivas com Algoritmos de Grafos
📌 Descrição
Este projeto tem como objetivo aplicar os conceitos de Grafos e Algoritmos de Caminho Mínimo (Dijkstra) em um sistema de localização de lojas de autopeças. Dado um endereço fornecido pelo usuário, o sistema utiliza geolocalização para encontrar a loja mais próxima, calcula o caminho entre as lojas e exibe as peças disponíveis.

Este projeto foi desenvolvido como parte da Sprint 4 da disciplina de Estrutura de Dados.

👥 Integrantes
Gabriel Borba - RM553187

Enzo Teles de Moura – RM553899

Gustavo Gouvêa Soares - RM553842

Henrique Rafael Gomes de Souza - RM553945

Pedro Henrique Mello Silva Alves - RM554223

🚀 Funcionalidades
Consulta de peças automotivas por localização

Integração com Google Maps API para geocodificação

Cálculo de distâncias geográficas usando a fórmula de Haversine

Representação de lojas e distâncias como um grafo ponderado

Algoritmo de Dijkstra otimizado para encontrar caminhos mínimos entre lojas

Exibição das peças disponíveis na loja mais próxima ao endereço do usuário

🧠 Tecnologias e Conceitos
Python 3

Grafos Ponderados

Algoritmo de Dijkstra

Fórmula de Haversine

Google Maps Geocoding API

Estruturas de Dados: Fila de prioridade (heap), dicionários, listas

Programação Orientada a Objetos

🧭 Como Funciona
O sistema armazena um banco de dados simulado de lojas e peças automotivas.

Ao digitar um endereço, a API do Google Maps retorna as coordenadas geográficas.

Com base nessas coordenadas, o sistema calcula a distância até cada loja.

O algoritmo de Dijkstra é usado para calcular o caminho mais curto entre as lojas.

O sistema exibe:

A loja mais próxima

A distância até ela

O caminho calculado

As peças disponíveis na loja

