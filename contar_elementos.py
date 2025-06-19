def contar_elementos(lista):
    if not lista:
        return 0
    if isinstance(lista[0], list):
        return contar_elementos(lista[0]) + contar_elementos(lista[1:])
    return 1 + contar_elementos(lista[1:])
