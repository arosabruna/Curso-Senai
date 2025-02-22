from app.controllers.clienteController import clienteController
from app.controllers.produtoController import produtoController

def exibir_menu():
    print("\n==== MENU ====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main ():
    cntrlCliente = clienteController()
    cntrlProduto = produtoController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção:")

        if opc == "1":
            nome = input("Nome do cliente:")
            email = input("E-mail:")
            idade = int(input("Idade:"))
            # Salvariamos no banco de dados #
            cntrlCliente.criar_cliente(nome, email, idade) 
            
        elif opc == "2":
            # Listar do banco de dados os clientes
            clientes = cntrlCliente.listar_clientes()
        
            for index, cliente in enumerate(clientes, 1):
                # index -> Posiçã atual do cliente listado
                # __str__ -> cliente => Cliente(nome"", email=", idade=="")
                print(f"{index}. {cliente}")

        elif opc == "3":
            nome = input("Nome do Produto:")
            preco = float(input("Preço:"))
            cntrlProduto.criar_produto(nome, preco) 

        elif opc == "4":
            # Listar do banco de daddos os produtos
            produtos = cntrlProduto.listar_produtos()
            for index, produto in enumerate(produtos, 1):
                print(f"{index}. {produto}")
           
            
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else: 
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# python main.py



