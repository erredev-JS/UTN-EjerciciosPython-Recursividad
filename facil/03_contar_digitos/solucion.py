def contar_digitos(n):
    if abs(n) < 10:
        return 1
    return 1 + contar_digitos(abs(n) // 10)
