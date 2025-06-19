def aplanar(lista):
    if not lista:
        return []
    if isinstance(lista[0], list):
        return aplanar(lista[0]) + aplanar(lista[1:])
    return [lista[0]] + aplanar(lista[1:])
