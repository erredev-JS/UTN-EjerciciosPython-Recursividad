def multiplicar(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiplicar(a, -b)
    return a + multiplicar(a, b - 1)
