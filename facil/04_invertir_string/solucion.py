def invertir_string(s):
    if s == "":
        return ""
    return invertir_string(s[1:]) + s[0]
