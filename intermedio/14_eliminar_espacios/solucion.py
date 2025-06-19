def eliminar_espacios(s):
    if not s:
        return ""
    if s[0] == " ":
        return eliminar_espacios(s[1:])
    return s[0] + eliminar_espacios(s[1:])
