def buscar(lista, objetivo):
    if not lista:
        return False
    if lista[0] == objetivo:
        return True
    return buscar(lista[1:], objetivo)
