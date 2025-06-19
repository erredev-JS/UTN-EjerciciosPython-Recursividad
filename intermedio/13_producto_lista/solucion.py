def producto_lista(lista):
    if not lista:
        return 1
    return lista[0] * producto_lista(lista[1:])
