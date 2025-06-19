def permutaciones(s):
    if len(s) <= 1:
        return [s]
    resultado = []
    for i, letra in enumerate(s):
        for p in permutaciones(s[:i] + s[i+1:]):
            resultado.append(letra + p)
    return resultado
