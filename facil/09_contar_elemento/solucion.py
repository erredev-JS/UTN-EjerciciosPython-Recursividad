def contar_elemento(lista, elem):
    if not lista:
        return 0
    return (1 if lista[0] == elem else 0) + contar_elemento(lista[1:], elem)
