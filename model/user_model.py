def login( usuarios_cadastrados, usuario ):
    for usuario_cadastrado in usuarios_cadastrados:
        if usuario["usuario"] == usuario_cadastrado["usuario"] and usuario["senha"] == usuario_cadastrado["senha"]:
            return usuario_cadastrado['id']
    return -1
                                 