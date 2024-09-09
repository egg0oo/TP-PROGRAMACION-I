def verificar_nombre(nombre):
    while not nombre.isalpha():
        print("El nombre debe estar únicamente compuesto por letras.")
        nombre = input("Intenta nuevamente: ")
    nombre = nombre.upper()
    return nombre