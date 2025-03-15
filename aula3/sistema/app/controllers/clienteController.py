from ..models.cliente import Cliente
from ..database.database import BancoFake

class clienteController:
    def __init__(self):
        # Coneção com o banco #
        self.db = BancoFake()

    def criar_cliente(self, nome, email, idade):
        # Criar o objeto cliente e salva no banco
        novo_cliente = Cliente(nome, email, idade)
        # Converter para dict (JSON)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        # Salvar no banco
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        """
        Retorna uma lista com todos os clientes
        """
        return self.db.listar_clientes()
    
    
