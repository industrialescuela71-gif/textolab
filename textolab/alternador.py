def alternar_mayusculas(texto):
    resultado = ""
    mayus = True
    for letra in texto:
        if letra.isalpha():
            resultado += letra.upper() if mayus else letra.lower()
            mayus = not mayus
        else:
            resultado += letra
    return resultado
