def nombrar(personaje):
    nombre = input("Ingresa el nombre: ")
    if verificar(nombre):
        return nombre.upper()
    else:
        print("El nombre es inválido. Intente nuevamente.")
        nombre = nombrar(personaje)
        return nombre.upper()

def verificar(nombre):
    if nombre.isalpha() == True:
        return True
    else:
        return False