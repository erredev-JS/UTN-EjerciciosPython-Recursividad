def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b - 1)
