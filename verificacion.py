def nombrar(personaje):
    nombre = input("Ingresa el nombre: ").upper()
    verificar = lambda nombre: nombre.isalpha()
    if verificar(nombre):
        return nombre
    else:
        print("El nombre es inválido. Intente nuevamente.")
        return nombrar(personaje)