import requests
import json
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self):
        self.base_url = "https://api-catalogo.redeancora.com.br/superbusca"
        self.token = None
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.is_authenticated = False
        # Credenciais padrão
        self.default_username = "superbusca"
        self.default_password = "superbusca"

    def login(self, username: str = None, password: str = None) -> bool:
        """Autenticar com a API e obter token"""
        try:
            # Usa as credenciais fornecidas ou as padrão
            username = username or self.default_username
            password = password or self.default_password

            # Ajustando o payload para o formato correto
            payload = {
                "grant_type": "password",
                "username": username,
                "password": password,
                "client_id": "superbusca",
                "client_secret": "superbusca"
            }

            print("\nTentando fazer login...")
            print(f"URL: {self.base_url}/auth/token")

            response = requests.post(
                f"{self.base_url}/auth/token",
                data=payload,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json"
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                self.token = data.get("access_token")
                if not self.token:
                    print("Erro: Token não encontrado na resposta")
                    return False
                    
                self.headers["Authorization"] = f"Bearer {self.token}"
                self.is_authenticated = True
                print("Login realizado com sucesso!")
                return True
            else:
                print(f"\nFalha no login:")
                print(f"Código de status: {response.status_code}")
                self.is_authenticated = False
                return False
        except Exception as e:
            print(f"\nErro durante o login:")
            print(f"Tipo do erro: {type(e).__name__}")
            print(f"Mensagem: {str(e)}")
            self.is_authenticated = False
            return False

    def check_auth(self) -> bool:
        """Verifica se o usuário está autenticado"""
        if not self.is_authenticated:
            print("\n⚠️ Você precisa fazer login primeiro!")
            return False
        return True

    def search_products(self, 
                       search_term: str,
                       page: int = 1,
                       page_size: int = 10,
                       filters: Optional[Dict[str, Any]] = None) -> Dict:
        """Buscar produtos com filtros opcionais"""
        if not self.check_auth():
            return {}

        payload = {
            "searchTerm": search_term,
            "page": page,
            "pageSize": page_size
        }

        if filters:
            payload.update(filters)

        try:
            response = requests.post(
                f"{self.base_url}/api/v2/products/search",
                json=payload,
                headers=self.headers
            )
            return response.json()
        except Exception as e:
            print(f"Erro na busca de produtos: {str(e)}")
            return {}

    def get_product_details(self, product_id: str) -> Dict:
        """Obter informações detalhadas de um produto específico"""
        if not self.check_auth():
            return {}

        try:
            response = requests.get(
                f"{self.base_url}/api/v2/products/{product_id}",
                headers=self.headers
            )
            return response.json()
        except Exception as e:
            print(f"Erro ao obter detalhes do produto: {str(e)}")
            return {}

    def get_categories(self) -> Dict:
        """Obter todas as categorias de produtos"""
        if not self.check_auth():
            return {}

        try:
            response = requests.get(
                f"{self.base_url}/api/v2/categories",
                headers=self.headers
            )
            return response.json()
        except Exception as e:
            print(f"Erro ao obter categorias: {str(e)}")
            return {}

    def get_brands(self) -> Dict:
        """Obter todas as marcas de produtos"""
        if not self.check_auth():
            return {}

        try:
            response = requests.get(
                f"{self.base_url}/api/v2/brands",
                headers=self.headers
            )
            return response.json()
        except Exception as e:
            print(f"Erro ao obter marcas: {str(e)}")
            return {}

def main():
    client = APIClient()
    
    # Força o login antes de qualquer operação
    print("\n" + "-"*30)
    print("Bem-vindo ao Sistema de Busca de Produtos")
    print("-"*30)
    
    # Tenta fazer login automaticamente com as credenciais padrão
    if client.login():
        while True:
            print("\n" + "="*50)
            print("Operações disponíveis:")
            print("1. Buscar produtos")
            print("2. Ver detalhes do produto")
            print("3. Listar categorias")
            print("4. Listar marcas")
            print("5. Sair")
            print("="*50)
            
            opcao = input("\nSelecione uma operação (1-5): ")
            
            if opcao == "1":
                termo_busca = input("Digite o termo de busca: ")
                pagina = int(input("Digite o número da página (padrão 1): ") or "1")
                tamanho_pagina = int(input("Digite o tamanho da página (padrão 10): ") or "10")
                
                filtros = {
                    "categoryId": input("Digite o ID da categoria (opcional): ") or None,
                    "brandId": input("Digite o ID da marca (opcional): ") or None,
                    "minPrice": float(input("Digite o preço mínimo (opcional): ") or "0"),
                    "maxPrice": float(input("Digite o preço máximo (opcional): ") or "999999")
                }
                
                filtros = {k: v for k, v in filtros.items() if v is not None}
                
                resultados = client.search_products(termo_busca, pagina, tamanho_pagina, filtros)
                print("\nResultados da busca:")
                print(json.dumps(resultados, indent=2, ensure_ascii=False))
                
            elif opcao == "2":
                id_produto = input("Digite o ID do produto: ")
                detalhes = client.get_product_details(id_produto)
                print("\nDetalhes do produto:")
                print(json.dumps(detalhes, indent=2, ensure_ascii=False))
                
            elif opcao == "3":
                categorias = client.get_categories()
                print("\nCategorias:")
                print(json.dumps(categorias, indent=2, ensure_ascii=False))
                
            elif opcao == "4":
                marcas = client.get_brands()
                print("\nMarcas:")
                print(json.dumps(marcas, indent=2, ensure_ascii=False))
                
            elif opcao == "5":
                print("\nObrigado por usar o sistema!")
                return
                
            else:
                print("\nOpção inválida! Por favor, tente novamente.")
    else:
        print("\nErro ao fazer login com as credenciais padrão!")
        print("Por favor, verifique se o servidor está acessível.")

if __name__ == "__main__":
    main() 