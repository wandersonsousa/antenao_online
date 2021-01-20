def login( usuarios_cadastrados, usuario ):
    for usuario_cadastrado in usuarios_cadastrados:
        if usuario == usuario_cadastrado:
            return True
    return False
