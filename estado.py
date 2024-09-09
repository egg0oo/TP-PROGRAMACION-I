def mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index):
    print("===== ESTADO ACTUAL =====")
    print(f"{enemigos[enemigo_index]}: {enemigos_hp[enemigo_index]} HP")
    for i in range(len(jugadores)):
        print(f"{jugadores[i]}: {jugadores_hp[i]} HP")
    print("==========================")