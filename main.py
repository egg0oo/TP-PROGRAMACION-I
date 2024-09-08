# JUEGO DE ROL: EL LEGADO PERDIDO

import random

def verificarnombre():
    tan = input("TANQUE: ")
    while not (tan.isalpha()):
        print("El nombre del TANQUE debe estar Ãºnicamente compuesto por letras.")
        tan = input("Intenta nuevamente: ")
    bru = input("BRUJO: ")
    while not (bru.isalpha()):
        print("El nombre del BRUJO debe estar Ãºnicamente compuesto por letras.")
        bru = input("Intenta nuevamente: ")
    ar = input("ARQUERO: ")
    while not (ar.isalpha()):
        print("El nombre del ARQUERO debe estar Ãºnicamente compuesto por letras.")
        ar = input("Intenta nuevamente: ")
    Mayusculas = lambda a, b, c: (a.upper(), b.upper(), c.upper())
    tan, bru, ar = Mayusculas(tan, bru, ar)
    return tan, bru, ar

def ataque():
    daño = random.randint(60, 100)
    return daño

def turno_jugador(jugador, jugador_hp, hp_enemigo):
    print(f"TURNO DE {jugador}")
    print("Acciones disponibles: Atacar - Bloquear - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Atacar", "Bloquear", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    if accion == "Atacar":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} ataca causando {daño} puntos de daño.")
    
    elif accion == "Bloquear":
        print(f"{jugador} bloquea el ataque.")
    
    elif accion == "Items":
        print("Items disponibles: Vendaje (60 HP), Poción (100 HP), Palo Distractor (-40 HP enemigo)")
        item = input("¿Qué ítem usarás?: ").capitalize()
        if item == "Vendaje":
            jugador_hp += 60
            print(f"{jugador} usa Vendaje y recupera 50 puntos de HP.")
        elif item == "Poción":
            jugador_hp += 100
            print(f"{jugador} usa Poción y recupera 80 puntos de HP.")
        elif item == "Palo distractor":
            daño = 40
            hp_enemigo -= daño
            print(f"{jugador} usa el Palo Distractor y causa {daño} puntos de daño al enemigo.")
        else:
            print("Ítem no válido.")
    
    return hp_enemigo, jugador_hp

def main():
    print("Nombra a tus personajes. Solo se permiten caracteres alfabeticos.")
    tan, bru, ar = verificarnombre()

    print(f"Tus personajes son {tan}, {bru} y {ar}",sep="")
    
    # Vida de los personajes
    TANQUE_HP = 350
    BRUJO_HP = 250
    ARQUERO_HP = 200
    jugadores = [tanque, brujo, arquero]
    jugadores_hp = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]
    
    # Enemigos y sus puntos de vida
    enemigos = ["Enemigo 1", "Enemigo 2", "Enemigo 3"]
    enemigos_hp = [400, 450, 600]
    enemigo_index = 0
    
    print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
    
    jugador_index = 0  # Comienza con el primer jugador
    
    while enemigo_index < len(enemigos) and sum(jugadores_hp) > 0:
        jugador_actual = jugadores[jugador_index]
        hp_enemigo = enemigos_hp[enemigo_index]
        
        # Turno del jugador
        hp_enemigo, jugadores_hp[jugador_index] = turno_jugador(jugador_actual, jugadores_hp[jugador_index], hp_enemigo)
        enemigos_hp[enemigo_index] = hp_enemigo
        
        if enemigos_hp[enemigo_index] <= 0:
            enemigos_hp[enemigo_index] = 0  # Evitar que HP sea negativo
            print(f"¡Has derrotado a {enemigos[enemigo_index]}!")
            enemigo_index += 1  # Pasamos al siguiente enemigo
            if enemigo_index < len(enemigos):
                print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
        else:
            print(f"{enemigos[enemigo_index]}: {enemigos_hp[enemigo_index]} HP")
        
        # Simulación de ataque enemigo
        if enemigo_index < len(enemigos):
            enemigo_ataque = random.randint(10, 40)
            jugador_atacado_index = random.randint(0, len(jugadores) - 1)
            jugadores_hp[jugador_atacado_index] -= enemigo_ataque
            jugadores_hp[jugador_atacado_index] = max(0, jugadores_hp[jugador_atacado_index])  # Evitar HP negativo
            print(f"{enemigos[enemigo_index]} ataca a {jugadores[jugador_atacado_index]} y causa {enemigo_ataque} de daño.")
            print(f"{jugadores[jugador_atacado_index]}: {jugadores_hp[jugador_atacado_index]} HP")
        
        jugador_index = (jugador_index + 1) % len(jugadores)
        
        # Si todos los personajes han sido derrotados
        if sum(jugadores_hp) == 0:
            print("¡Has sido derrotado por los enemigos!")
    
    if enemigo_index == len(enemigos) and sum(jugadores_hp) > 0:
        print("¡Has derrotado a todos los enemigos!")

if __name__ == "__main__":
    main()
