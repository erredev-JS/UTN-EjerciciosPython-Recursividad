def contar_vocales(palabra):
    if not palabra:
        return 0
    return (1 if palabra[0].lower() in 'aeiou' else 0) + contar_vocales(palabra[1:])
