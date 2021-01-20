def menu_inicial():
    print("*-" * 40)
    print("Digite 1 para fazer login e acessar a loja")
    print("Digite 0 para sair do programa")

def menu_formulario_login():
    print("Digite os dados abaixo para realizar o login")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    return {
        "usuario": usuario,
        "senha": senha
    }

