def nombrar(personaje):
    nombre = input("Ingresa el nombre: ")
    if verificar(nombre):
        return nombre
    else:
        print("El nombre es inválido. Intente nuevamente.")
        nombre = nombrar(personaje)
        return nombre

def verificar(nombre):
    if nombre.isalpha() == True:
        return True
    else:
        return False