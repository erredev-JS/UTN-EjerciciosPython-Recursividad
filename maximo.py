def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max
