from ..model.usuario_model import UsuarioModel

def listar_usuarios():
    # Exibir a lista de usuarios
    model = UsuarioModel()
    usuarios = model.get_all_user()
    model.close_connection()
    return usuarios

def cadastrar_usuario(nome, idade, email):
    # Cadastrar o Usuario 
    model = UsuarioModel()
    # Verificar se email já existe
    if model.get_user_by_email(email):
        model.close.connection()
        return "Email já existe, tente novemente"
    # Se não existir, cadastrar 
    novo_id = model.insert_user(nome, idade, email)
    model.close_connection()
    return novo_id

def atualizar_usuario(usuario_id, nome, idade, email):
    model = UsuarioModel()
    linhas_afetadas = model.update_user_by_id(usuario_id, nome, idade, email)
    model.close_connection()
    return linhas_afetadas

def remover_usuario(usuario_id):
    model = UsuarioModel()
    linhas_afetadas = model.delete_user_by_id(usuario_id)
    model.close_connection()
    return linhas_afetadas

def obter_usuario(usuario_id):
    model = UsuarioModel()
    usuario = model.get_product_by_id(usuario_id)
    model.close_connection()
    return usuario 


