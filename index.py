from view import menu_principal
from model import user_model

usuarios = [
    {
        "usuario": "admin",
        "senha": "admin"
    }
]


def main():
    menu_principal.menu_inicial()
    selecao_menu_principal = int(input(">> "))

    if selecao_menu_principal == 0:
        return {"msg":"parado"}
    
    if selecao_menu_principal == 1:
        entrada_dados_usuario = menu_principal.menu_formulario_login()
        usuario_logado = user_model.login(usuarios, entrada_dados_usuario)
        
        if usuario_logado:
            print("LOGADO COM SUCESSO !")
        else:
            return {"msg":"falha login"}

    return {"msg":"ok"}

if __name__ == "__main__":
    while True:
        programa_estado_atual = main()    

        if programa_estado_atual["msg"] == "parado":
            break
        if programa_estado_atual["msg"] == "falha login":
            continue