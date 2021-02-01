from view import menu_principal
from model import user_model

usuarios = [
    {
        "id":0,
        "usuario": "admin",
        "senha": "admin",
        "produtos_comprados": [

        ]
    }
]

produtos = [
    {
        "nome": "Samsung Galaxy J7",
        "preco":"R$ 1499,00",
        "id":0
    },
    {
        "nome": "Aparador de Grama",
        "preco": "R$ 500,00",
        "id":1
    },
    {
        "nome":"Boneco Fofão com agulhas inclusas",
        "preco": "R$ 135,50",
        "id":2
    }
]

usuario_logado = False
selecao_menu_principal = 1
usuario_id = None

def main():
    global usuario_logado, selecao_menu_principal, usuario_id
    
    if not usuario_logado:
        menu_principal.menu_inicial()
        selecao_menu_principal = int(input(">> "))

        if selecao_menu_principal == 0:
            return {"msg":"parado"}
    
    if selecao_menu_principal == 1:
        if not usuario_logado:
            entrada_dados_usuario = menu_principal.menu_formulario_login()
            usuario_id = user_model.login(usuarios, entrada_dados_usuario)

        if usuario_id != -1:
            usuario_logado = True
            menu_principal.menu_pagina_inicial_loja( produtos )
            id = int(input("PARA COMPRAR DIGITE O ID DO PRODUTO DESEJADO >> "))
            for usuario in usuarios:
                if usuario['id'] == usuario_id:
                    for produto in produtos:
                        if produto['id'] == id:
                            usuario['produtos_comprados'].append( produto )
                            
                            comprar_novamente = int(input("Para comprar mais digite 1 \nPara sair digite 0 >> "))

                            if comprar_novamente == 0:
                                usuario_logado = False
        else:
            return {"msg":"falha login"}

    return {"msg":"ok"}

if __name__ == "__main__":
    while True:
        programa_estado_atual = main()    

        if programa_estado_atual["msg"] == "parado":
            print(programa_estado_atual)
            break
        if programa_estado_atual["msg"] == "falha login":
            print(programa_estado_atual)
            continue