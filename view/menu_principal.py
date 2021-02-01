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

def lista_produtos( produtos ):
    for produto in produtos:
        print("-*" * 20)
        print("Nome: " + produto["nome"])
        print("Preço: " + produto["preco"])
        print("id: " + str(produto["id"]) )
    
def menu_pagina_inicial_loja( produtos ):
    print("-" * 20)
    lista_produtos( produtos )