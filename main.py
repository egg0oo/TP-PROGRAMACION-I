# JUEGO DE ROL: EL LEGADO PERDIDO

import random

def verificar_nombre(nombre):
    while not nombre.isalpha():
        print("El nombre debe estar únicamente compuesto por letras.")
        nombre = input("Intenta nuevamente: ")
    nombre = nombre.upper()
    return nombre

def ataque():
    daño = random.randint(60, 100)
    return daño

def usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print("Items disponibles: Vendaje (60 HP), Poción (100 HP), Palo Distractor (-40 HP enemigo)")
    item = input("¿Qué ítem usarás?: ").capitalize()
    if item == "Vendaje":
        jugador_hp += 60
        print(f"{jugador} usa Vendaje y recupera 60 puntos de HP.")
    elif item == "Poción":
        jugador_hp += 100
        print(f"{jugador} usa Poción y recupera 100 puntos de HP.")
    elif item == "Palo Distractor":
        daño = 40
        hp_enemigo -= daño
        print(f"{jugador} usa el Palo Distractor y causa {daño} puntos de daño al enemigo.")
    else:
        print("Ítem no válido.")
    
    jugador_hp = min(jugador_hp, hp_maximo)  # Limitar HP al máximo permitido
    return jugador_hp, hp_enemigo

def turno_jugador(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print(f"===== TURNO DE {jugador} =====")
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
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo)
    
    return hp_enemigo, jugador_hp

def mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index):
    print("===== ESTADO ACTUAL =====")
    print(f"{enemigos[enemigo_index]}: {enemigos_hp[enemigo_index]} HP")
    for i in range(len(jugadores)):
        print(f"{jugadores[i]}: {jugadores_hp[i]} HP")
    print("==========================")

def regenerar_vida(jugadores_hp, vida_inicial):
    print("Regenerando vida de los personajes...")
    for i in range(len(jugadores_hp)):
        jugadores_hp[i] = vida_inicial[i]
    print("¡La vida de todos los personajes ha sido regenerada!")

def ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp):
    enemigo_ataque = random.randint(10, 40)
    
    jugadores_vivos = [i for i in range(len(jugadores_hp)) if jugadores_hp[i] > 0]

    if not jugadores_vivos:
        print("¡No quedan jugadores con vida!")
        return jugadores_hp

    jugador_atacado_index = random.choice(jugadores_vivos)  # NO VIMOS!!! PERO DEJENLO. Selecciona un elemento al azar en una lista. Queria usar random.randint(0,2) pero no conseguí que no seleccione a un personaje con 0HP
    
    jugadores_hp[jugador_atacado_index] -= enemigo_ataque
    jugadores_hp[jugador_atacado_index] = max(0, jugadores_hp[jugador_atacado_index])  # Evitar HP negativo
    
    print(f"{enemigos[enemigo_index]} ataca a {jugadores[jugador_atacado_index]} y causa {enemigo_ataque} de daño.")
    print(f"{jugadores[jugador_atacado_index]}: {jugadores_hp[jugador_atacado_index]} HP")
    
    return jugadores_hp

def main():
    print("Nombra a tus personajes. Solo se permiten caracteres alfabéticos.")
    n = input("TANQUE: ")
    tanque = verificar_nombre(n)
    n = input("BRUJO: ")
    brujo = verificar_nombre(n)
    n = input("ARQUERO: ")
    arquero = verificar_nombre(n)
    
    print(f"Tus personajes son {tanque}, {brujo} y {arquero}")
    
    # Vida de los personajes
    TANQUE_HP = 350
    BRUJO_HP = 250
    ARQUERO_HP = 200
    jugadores = [tanque, brujo, arquero]
    jugadores_hp = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]
    vida_inicial = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]
    
    # Enemigos y sus puntos de vida
    enemigos = ["Enemigo 1", "Enemigo 2", "Enemigo 3"]
    enemigos_hp = [400, 450, 600]
    enemigo_index = 0
    
    print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
    
    jugador_index = 0  # Comienza con el primer jugador
    
    while enemigo_index < len(enemigos) and sum(jugadores_hp) > 0:
        jugador_actual = jugadores[jugador_index]
        hp_enemigo = enemigos_hp[enemigo_index]
        hp_maximo = [TANQUE_HP, BRUJO_HP, ARQUERO_HP][jugador_index]  # Obtener el HP máximo del jugador actual
        
        # Mostrar el estado actual antes del turno
        mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index)
        
        # Turno del jugador
        hp_enemigo, jugadores_hp[jugador_index] = turno_jugador(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo)
        enemigos_hp[enemigo_index] = hp_enemigo
        
        if enemigos_hp[enemigo_index] <= 0:
            enemigos_hp[enemigo_index] = 0  # Evitar que HP sea negativo
            print(f"¡Has derrotado a {enemigos[enemigo_index]}!")
            enemigo_index += 1
            if enemigo_index < len(enemigos):
                print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
                regenerar_vida(jugadores_hp, vida_inicial)  # Regenerar vida después de cada combate
        else:
            print(f"{enemigos[enemigo_index]}: {enemigos_hp[enemigo_index]} HP")
        
        if enemigo_index < len(enemigos):
            jugadores_hp = ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp)
        
        jugador_index = (jugador_index + 1) % len(jugadores)  # Reinicia el turno cuando llega al último jugador
    
    if enemigo_index == len(enemigos) and sum(jugadores_hp) > 0:
        print("¡Has derrotado a todos los enemigos!")
    else:
        print("¡Has sido derrotado por los enemigos!")
        
if __name__ == "__main__":
    main()
