import json  # lidar com arquivo JSON
from pathlib import Path  # lidar com caminhos do WIN

class BancoFake:
        
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        caso não exista, inicia com dados vazios
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # salvando dados que já existem no arquivo na variável de dados
                self.dados = json.load(data)
        else:
            self._salvar()
    
    def _salvar(self):
        """
        Salvar o conteúdo de self.dados no arquivo JSON
        """
        # Abrindo arquivo no modo W (escrita)
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # realizando DUMP (Python para JSON) para salvar no banco
            json.dump(self.dados, data, ensure_ascii=False, indent=4)
        
    
    def adicionar_cliente(self, cliente_dict):
        """
        Adiciona um cliente ao banco de dados, gerando um ID sequencial automaticamente.
        """
        # Gera o próximo ID como o tamanho atual + 1
        cliente_dict["id"] = len(self.dados["clientes"]) + 1
        self.dados["clientes"].append(cliente_dict)
        self._salvar()
        print(f"Cliente adicionado com ID {cliente_dict['id']}")

    def listar_clientes(self):
        return self.dados["clientes"]
    
    def excluir_cliente(self, cliente_id):
        """
        Exclui um cliente pelo ID fornecido.
        """
        clientes_iniciais = len(self.dados["clientes"])
        # Filtra a lista de clientes para remover o cliente com o ID fornecido
        self.dados["clientes"] = [
            cliente for cliente in self.dados["clientes"] 
            if cliente.get("id") != cliente_id
        ]
        if len(self.dados["clientes"]) < clientes_iniciais:
            print(f"Cliente com ID {cliente_id} excluído com sucesso.")
            self._salvar()
        else:
            print(f"Nenhum cliente com ID {cliente_id} foi encontrado.")
    

    def adicionar_produto(self, produto_dict):
        """
        Adiciona um produto ao banco de dados, gerando um ID sequencial automaticamente.
        """
        # Gera o próximo ID como o tamanho atual + 1
        produto_dict["id"] = len(self.dados["produtos"]) + 1
        self.dados["produtos"].append(produto_dict)
        self._salvar()
        print(f"Produto adicionado com ID {produto_dict['id']}")
    
    def listar_produtos(self):
        return self.dados["produtos"]

    def excluir_produto(self, produto_id):
        """
        Exclui um produto pelo ID fornecido.
        """
        produtos_iniciais = len(self.dados["produtos"])
        # Filtra a lista de produtos para remover o produto com o ID fornecido
        self.dados["produtos"] = [
            produto for produto in self.dados["produtos"] 
            if produto.get("id") != produto_id
        ]
        if len(self.dados["produtos"]) < produtos_iniciais:
            print(f"Produto com ID {produto_id} excluído com sucesso.")
            self._salvar()
        else:
            print(f"Nenhum produto com ID {produto_id} foi encontrado.")
    
