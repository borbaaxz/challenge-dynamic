# -*- coding: utf-8 -*-
"""
Sprint 4 - Grafos e algoritmo de menor caminho
Integrantes:
Gabriel Borba - RM553187
Enzo Teles de Moura - RM553899
Gustavo Gouvêa Soares - RM553842
Henrique Rafael Gomes de Souza - RM553945
Pedro Henrique Mello Silva Alves - RM554223
"""

from collections import deque
import bisect
import heapq
import requests
from math import radians, sin, cos, sqrt, atan2

# =============================================
# CONFIGURAÇÕES GLOBAIS
# =============================================
API_KEY = "AIzaSyCy65CSuPVlNcaX-7CD7p5Oth1tZ-iJOCc" 

# =============================================
# BANCO DE DADOS COMPLETO
# =============================================

lojas = [
    {"id": "L1", "nome": "AutoPeças Centro", "endereco": "Av. Paulista, 1000, São Paulo, SP", 
     "latitude": -23.5637, "longitude": -46.6529},
    {"id": "L2", "nome": "Peças Zona Sul", "endereco": "Rua Oscar Freire, 200, São Paulo, SP", 
     "latitude": -23.5560, "longitude": -46.6743},
    {"id": "L3", "nome": "Mecânica Norte", "endereco": "Av. Inajar de Souza, 300, São Paulo, SP", 
     "latitude": -23.4949, "longitude": -46.6221}
]
pecas = [
    {"id": "P1", "descricao": "Motor Completo", "ano": 2020, "preco": 25000, "placa": "ABC1234", "loja_id": "L1"},
    {"id": "P2", "descricao": "Freio a Disco", "ano": 2018, "preco": 600, "placa": "XYZ5678", "loja_id": "L2"},
    {"id": "P3", "descricao": "Radiador", "ano": 2019, "preco": 1200, "placa": "DEF3456", "loja_id": "L3"},
    {"id": "P4", "descricao": "Filtro de Óleo", "ano": 2021, "preco": 80, "placa": "GHI7890", "loja_id": "L1"},
    {"id": "P5", "descricao": "Correia Dentada", "ano": 2017, "preco": 350, "placa": "JKL1234", "loja_id": "L2"},
    {"id": "P6", "descricao": "Amortecedor", "ano": 2020, "preco": 500, "placa": "MNO5678", "loja_id": "L3"},
    {"id": "P7", "descricao": "Catalisador", "ano": 2019, "preco": 1300, "placa": "PQR3456", "loja_id": "L1"},
    {"id": "P8", "descricao": "Alternador", "ano": 2016, "preco": 950, "placa": "STU7890", "loja_id": "L2"},
    {"id": "P9", "descricao": "Embreagem", "ano": 2018, "preco": 800, "placa": "VWX1234", "loja_id": "L3"},
    {"id": "P10", "descricao": "Cilindro Mestre", "ano": 2021, "preco": 400, "placa": "YZA5678", "loja_id": "L1"},
    {"id": "P11", "descricao": "Vela de Ignição", "ano": 2017, "preco": 40, "placa": "BCD3456", "loja_id": "L2"},
    {"id": "P12", "descricao": "Caixa de Direção", "ano": 2022, "preco": 2200, "placa": "EFG7890", "loja_id": "L3"},
    {"id": "P13", "descricao": "Escapamento", "ano": 2018, "preco": 1000, "placa": "HIJ1234", "loja_id": "L1"},
    {"id": "P14", "descricao": "Parafuso", "ano": 2021, "preco": 10, "placa": "KLM5678", "loja_id": "L2"},
    {"id": "P15", "descricao": "Módulo de Injeção", "ano": 2019, "preco": 3500, "placa": "NOP3456", "loja_id": "L3"},
    {"id": "P16", "descricao": "Bateria", "ano": 2020, "preco": 450, "placa": "QRS7890", "loja_id": "L1"},
    {"id": "P17", "descricao": "Pneu", "ano": 2019, "preco": 500, "placa": "TUV1234", "loja_id": "L2"},
    {"id": "P18", "descricao": "Caixa de Marchas", "ano": 2022, "preco": 3500, "placa": "WXY5678", "loja_id": "L3"},
    {"id": "P19", "descricao": "Disco de Embreagem", "ano": 2018, "preco": 350, "placa": "ZAB3456", "loja_id": "L1"},
    {"id": "P20", "descricao": "Sensor de Oxigênio", "ano": 2019, "preco": 250, "placa": "CDE7890", "loja_id": "L2"},
    {"id": "P21", "descricao": "Junta Homocinética", "ano": 2021, "preco": 750, "placa": "FGH1234", "loja_id": "L3"},
    {"id": "P22", "descricao": "Correia Poly V", "ano": 2020, "preco": 150, "placa": "IJK5678", "loja_id": "L1"},
    {"id": "P23", "descricao": "Bomba d'Água", "ano": 2019, "preco": 450, "placa": "LMN3456", "loja_id": "L2"},
    {"id": "P24", "descricao": "Filtro de Ar", "ano": 2018, "preco": 30, "placa": "OPQ7890", "loja_id": "L3"},
    {"id": "P25", "descricao": "Cilindro de Roda", "ano": 2020, "preco": 220, "placa": "RST1234", "loja_id": "L1"},
    {"id": "P26", "descricao": "Kit de Embrague", "ano": 2021, "preco": 950, "placa": "UVW5678", "loja_id": "L2"},
    {"id": "P27", "descricao": "Termostato", "ano": 2019, "preco": 120, "placa": "XYZ3456", "loja_id": "L3"},
    {"id": "P28", "descricao": "Bobina de Ignição", "ano": 2021, "preco": 200, "placa": "ABC7890", "loja_id": "L1"},
    {"id": "P29", "descricao": "Sensor de Velocidade", "ano": 2018, "preco": 150, "placa": "DEF1234", "loja_id": "L2"},
    {"id": "P30", "descricao": "Eixo Cardan", "ano": 2022, "preco": 2500, "placa": "GHI5678", "loja_id": "L3"},
]


# =============================================
# IMPLEMENTAÇÃO DO GRAFO
# =============================================

class Grafo:
    """Classe para representação de grafos ponderados"""
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino, peso, bidirecional=False):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.vertices[origem].append((destino, peso))
        if bidirecional:
            self.vertices[destino].append((origem, peso))

# =============================================
# FUNÇÕES DE GEOLOCALIZAÇÃO
# =============================================

def obter_coordenadas(endereco):
    """Obtém coordenadas geográficas usando Google Maps API"""
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={API_KEY}"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                return location['lat'], location['lng']
        print("Erro: Endereço não encontrado ou API indisponível")
        return None, None
    except Exception as e:
        print(f"Erro na conexão: {str(e)}")
        return None, None

def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula distância em km usando fórmula de Haversine"""
    R = 6371  # Raio da Terra em km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

# =============================================
# ALGORITMO DIJKSTRA
# =============================================

def dijkstra(grafo, inicio):
    """Implementação otimizada com heap prioritário"""
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    caminho = {inicio: []}

    while fila_prioridade:
        dist_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if dist_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo.vertices.get(vertice_atual, []):
            distancia = dist_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = caminho[vertice_atual] + [vertice_atual]
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias, caminho

# =============================================
# FUNÇÕES ADICIONAIS IMPLEMENTADAS
# =============================================

def inicializar_grafo_com_lojas():
    """Cria grafo com conexões reais entre as lojas"""
    grafo = Grafo()
    
    # Adiciona lojas como vértices
    for loja in lojas:
        grafo.adicionar_vertice(loja['id'])
    
    # Cria conexões bidirecionais entre todas as lojas
    for i in range(len(lojas)):
        for j in range(i + 1, len(lojas)):
            distancia = calcular_distancia(
                lojas[i]['latitude'], lojas[i]['longitude'],
                lojas[j]['latitude'], lojas[j]['longitude']
            )
            grafo.adicionar_aresta(
                lojas[i]['id'], lojas[j]['id'], distancia, bidirecional=True
            )
    
    return grafo

def encontrar_loja_proxima(endereco_usuario):
    """Encontra a loja mais próxima usando Dijkstra"""
    user_lat, user_lon = obter_coordenadas(endereco_usuario)
    if not user_lat or not user_lon:
        return None
    
    # Calcula distância direta para todas as lojas
    distancias_diretas = []
    for loja in lojas:
        distancia = calcular_distancia(
            user_lat, user_lon,
            loja['latitude'], loja['longitude']
        )
        distancias_diretas.append((distancia, loja))
    
    # Encontra a mais próxima para inicialização
    distancias_diretas.sort()
    loja_mais_proxima = distancias_diretas[0][1]
    
    # Calcula caminho usando Dijkstra
    distancias, caminhos = dijkstra(grafo_lojas, loja_mais_proxima['id'])
    caminho_completo = caminhos[loja_mais_proxima['id']] + [loja_mais_proxima['id']]
    
    # Obtém peças da loja
    pecas_loja = [p for p in pecas if p['loja_id'] == loja_mais_proxima['id']]
    
    return {
        'loja': loja_mais_proxima,
        'distancia': distancias_diretas[0][0],
        'caminho': caminho_completo,
        'pecas': pecas_loja
    }

# =============================================
# SISTEMA DE MENU COMPLETO E CORRIGIDO
# =============================================

fila_compras = deque()
total = 0.0
historico_pedidos = []
pecas_ordenadas = sorted(pecas, key=lambda x: x['descricao'].lower())

def menu_principal():
    """Sistema completo de gerenciamento"""
    global total, pecas_ordenadas
    
    while True:
        print("\n" + "="*50)
        print("🏎️ SISTEMA DE PEÇAS AUTOMOTIVAS - SPRINT 4")
        print("1. Adicionar pedido")
        print("2. Processar pedidos")
        print("3. Buscar peças por faixa de preço")
        print("4. Buscar K peças mais caras/baratas")
        print("5. Autocompletar busca")
        print("6. Encontrar loja mais próxima")
        print("7. Sair")
        
        opcao = input("\n🔘 Selecione uma opção: ").strip()
        
        # Opção 1 - Adicionar pedido
        if opcao == "1":
            print("\n🛒 ADICIONAR PEDIDO")
            while True:
                id_peca = input("Digite o ID da peça (ex: P1) ou 'sair': ").strip().upper()
                if id_peca.lower() == 'sair':
                    break
                
                peca = next((p for p in pecas if p["id"] == id_peca), None)
                
                if peca:
                    try:
                        quantidade = int(input(f"Quantidade para {peca['descricao']}: "))
                        if quantidade <= 0:
                            raise ValueError
                    except ValueError:
                        print("❌ Quantidade inválida! Use números inteiros positivos")
                        continue
                    
                    # Atualizar fila e total
                    fila_compras.append({
                        'id': peca['id'],
                        'descricao': peca['descricao'],
                        'preco_unitario': peca['preco'],
                        'quantidade': quantidade,
                        'subtotal': peca['preco'] * quantidade
                    })
                    total += peca['preco'] * quantidade
                    print(f"✅ {quantidade}x {peca['descricao']} adicionado(s)")
                    print(f"🛒 Total parcial: R$ {total:.2f}\n")
                else:
                    print("❌ Peça não encontrada! IDs válidos: P1-P30\n")

        # Opção 2 - Processar pedidos
        elif opcao == "2":
            if not fila_compras:
                print("\n🛒 Carrinho vazio!")
                continue

            print("\n💰 RESUMO DO PEDIDO")
            print("-"*60)
            print(f"{'ID':<5}{'Descrição':<25}{'Qtd':<5}{'Unitário':<12}{'Subtotal':<10}")
            print("-"*60)
            for item in fila_compras:
                print(f"{item['id']:<5}{item['descricao']:<25}{item['quantidade']:<5}"
                      f"R${item['preco_unitario']:<10.2f}R${item['subtotal']:>8.2f}")
            print("-"*60)
            print(f"💵 TOTAL A PAGAR: R$ {total:>47.2f}\n")

            confirmacao = input("Confirmar pagamento (S/N)? ").strip().lower()
            if confirmacao == 's':
                historico_pedidos.extend(fila_compras.copy())
                fila_compras.clear()
                total = 0.0
                print("\n✅ Pagamento realizado! Recibo:")
                for item in historico_pedidos[-1]:
                    print(f"  {item['id']} - {item['descricao']} x{item['quantidade']}")
            else:
                print("\n❌ Pagamento cancelado")

        # Opção 3 - Busca por preço
        elif opcao == "3":
            print("\n🔍 BUSCA POR FAIXA DE PREÇO")
            try:
                minimo = float(input("Valor mínimo (R$): "))
                maximo = float(input("Valor máximo (R$): "))
                if minimo < 0 or maximo < minimo:
                    raise ValueError
            except:
                print("❌ Valores inválidos! Use números decimais positivos")
                continue

            resultados = [p for p in pecas if minimo <= p['preco'] <= maximo]
            print(f"\n📊 Resultados ({len(resultados)} peças):")
            for p in sorted(resultados, key=lambda x: x['preco']):
                print(f"  {p['id']}: {p['descricao']:<30} R${p['preco']:>8.2f}")

        # Opção 4 - Top K peças
        elif opcao == "4":
            print("\n📈 TOP K PEÇAS")
            try:
                k = int(input("Quantidade de peças (K): "))
                tipo = input("Tipo ([C]aras/[B]aratas): ").lower()
                if k <= 0 or tipo not in ['c', 'b']:
                    raise ValueError
            except:
                print("❌ Entrada inválida! K deve ser > 0 e tipo C/B")
                continue

            reverse = tipo == 'c'
            resultados = sorted(pecas, key=lambda x: x['preco'], reverse=reverse)[:k]
            print(f"\n🏆 Top {k} peças mais {'caras' if reverse else 'baratas'}:")
            for i, p in enumerate(resultados, 1):
                print(f"{i:>2}. {p['descricao']:<30} R${p['preco']:>8.2f}")

        # Opção 5 - Autocompletar
        elif opcao == "5":
            print("\n🔎 AUTOCOMPLETAR BUSCA")
            termo = input("Digite parte da descrição: ").strip().lower()
            
            sugestoes = []
            for p in pecas:
                if termo in p['descricao'].lower():
                    bisect.insort(sugestoes, (p['descricao'].lower(), p))
            
            if sugestoes:
                print(f"\n🔍 {len(sugestoes)} sugestões para '{termo}':")
                for _, p in sugestoes:
                    print(f"  • {p['id']}: {p['descricao']} (R${p['preco']:.2f})")
            else:
                print("❌ Nenhuma correspondência encontrada")
        
        # Opção 6 - Loja próxima (atualizada)
        elif opcao == "6":
            endereco = input("\n📍 Digite seu endereço completo: ").strip()
            if not endereco:
                print("❌ Endereço não pode ser vazio!")
                continue
            
            resultado = encontrar_loja_proxima(endereco)
            
            if resultado:
                print("\n" + "="*50)
                print(f"🏁 MELHOR OPÇÃO: {resultado['loja']['nome']}")
                print(f"📐 Distância: {resultado['distancia']:.2f} km")
                print(f"🗺️ Caminho sugerido: {' → '.join(resultado['caminho'])}")
                print(f"📦 Peças disponíveis ({len(resultado['pecas'])} itens):")
                for peca in resultado['pecas'][:5]:
                    print(f"  • {peca['descricao']} (R${peca['preco']:.2f})")
                print("="*50)
            else:
                print("\n❌ Nenhuma loja encontrada ou erro de conexão")

         # Opção 7 - Sair
        elif opcao == "7":
            print("\n🚗 Obrigado por usar nosso sistema!")
            break
        
        else:
            print("\n⚠️ Opção inválida!")

# =============================================
# INICIALIZAÇÃO DO SISTEMA
# =============================================
if __name__ == "__main__":
    menu_principal()