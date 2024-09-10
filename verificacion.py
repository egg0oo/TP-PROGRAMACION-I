def verificarnombre():
    tan = input("TANQUE: ")
    while not (tan.isalpha()):
        print("El nombre del TANQUE debe estar únicamente compuesto por letras.")
        tan = input("Intenta nuevamente: ")
    bru = input("BRUJO: ")
    while not (bru.isalpha()):
        print("El nombre del BRUJO debe estar únicamente compuesto por letras.")
        bru = input("Intenta nuevamente: ")
    ar = input("ARQUERO: ")
    while not (ar.isalpha()):
        print("El nombre del ARQUERO debe estar únicamente compuesto por letras.")
        ar = input("Intenta nuevamente: ")
    Mayusculas = lambda a, b, c: (a.upper(), b.upper(), c.upper())
    tan, bru, ar = Mayusculas(tan, bru, ar)
    return tan, bru, ar