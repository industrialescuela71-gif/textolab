from textolab import invertir_texto, contar_vocales, alternar_mayusculas

def main():
    texto = input("Ingrese un texto: ")

    print("\n--- Resultados ---")
    print(f"Texto invertido: {invertir_texto(texto)}")
    print(f"Cantidad de vocales: {contar_vocales(texto)}")
    print(f"Texto alternado: {alternar_mayusculas(texto)}")

if __name__ == "__main__":
    main()
