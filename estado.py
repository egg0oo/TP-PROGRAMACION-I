def mostrar_estado(personajes, enemigos, enemigo_actual):
    print()
    print("===== ESTADO ACTUAL =====")    
    for nombre in personajes:
        print(f"{nombre}: {personajes[nombre]['vida']} HP")
    print(f"{enemigo_actual}: {enemigos[enemigo_actual]['vida']} HP")
    print("==========================")
    print()