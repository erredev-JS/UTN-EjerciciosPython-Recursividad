def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])
