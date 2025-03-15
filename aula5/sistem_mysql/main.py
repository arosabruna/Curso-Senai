
from src.controller import usuario_controller
def exibir_menu():
    print("\nBANCO DE USUARIOS!")
    print("\n=== MENU ===")
    print("1 - Cadastrar Usuario")
    print("2 - Listar Usuario")
    print("3 - Atualizar Usuario")
    print("4 - Deletar Usuario")
    print("5 - Buscar Usuario unico")
    print("0 - Sair")
   
def listar_usuarios():
    print("\n--- Lista de Usuarios ---")
    usuarios = usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']} ")
    else:
        print("Não existe usuarios cadastrados")

def cadastrar_usuario():
    print("\n---cadastrar usuario---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")
    novo_id = usuario_controller.cadastrar_usuario(nome, idade, email)
    if novo_id == "Erro: Email já cadastrado!":
        print(novo_id) 
    else:
        print(f"Usuario cadastrado com sucesso com o novo ID {novo_id}.")

def atualizar_usuario():
    print("\nATUALIZANDO O USUARIO")
    usuario_id = input("Digite o ID do usuario: ")
    nome = input("Digite o nome do usuario: ")
    idade = input("Digite a idade do usuario: ")
    email = input("Digite o email do usuario: ")

    linhas = usuario_controller.atualizar_usuario(usuario_id, nome, idade, email)
    if linhas > 0: # quantidade de linhas modificadas
        print("Usuario atualizado com sucesso!")
    else:
        print("Nenhum usuario foi atualizado")

# main -> Inicializar o projeto
def main():
    # While True -> Repetir mesmo que a opção digitada esteja errada
    while True:

        exibir_menu()
        opc = input("Escolha uma opção:")

        if opc == "1":
            cadastrar_usuario()
        elif opc =="2":
            listar_usuarios()
        elif opc =="3":
            atualizar_usuario()
        elif opc =="6":
            print("Saindo do sistema...")
            # sys.exit(0)
        else:
            print("Opção Inválida, tente novamente...")

if __name__ == '__main__':
    main()