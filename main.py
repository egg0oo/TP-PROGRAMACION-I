from verificacion import verificar_nombre
from estado import mostrar_estado
import random

def ataque():
    daño = random.randint(60, 100)
    return daño

def usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print("Items disponibles: Vendaje (60 HP), Poción (100 HP), Palo (el enemigo perderá su turno)")
    item = input("¿Qué ítem usarás?: ").capitalize()
    palo_activo = False
    if item == "Vendaje":
        jugador_hp += 60
        print(f"{jugador} usa Vendaje y recupera 60 puntos de HP.")
    elif item == "Poción":
        jugador_hp += 100
        print(f"{jugador} usa Poción y recupera 100 puntos de HP.")
    elif item == "Palo":
        palo_activo = True
        print(f"{jugador} usa el Palo y el enemigo perderá su turno.")
    else:
        print("Ítem no válido.")
    
    jugador_hp = min(jugador_hp, hp_maximo)  # Limitar HP al máximo permitido
    return jugador_hp, hp_enemigo, palo_activo

def turno_tanque(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print(f"===== TURNO DE {jugador} (TANQUE) =====")
    print("Acciones disponibles: Atacar - Bloquear - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Atacar", "Bloquear", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    palo_activo = False  # Definir la variable aquí

    if accion == "Atacar":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} ataca causando {daño} puntos de daño.")
    
    elif accion == "Bloquear":
        print(f"{jugador} bloquea el ataque.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo, palo_activo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo)
    
    return hp_enemigo, jugador_hp, palo_activo

def turno_brujo(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print(f"===== TURNO DE {jugador} (BRUJO) =====")
    print("Acciones disponibles: Bola de fuego - Magia negra - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Bola de fuego", "Magia negra", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    palo_activo = False  # Definir la variable aquí

    if accion == "Bola de fuego":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} usa bola de fuego causando {daño} puntos de daño.")
    
    elif accion == "Magia negra":
        daño = ataque()
        hp_enemigo -= daño + 20
        print(f"{jugador} usa un hechizo de magia negra causando {daño + 20} puntos de daño.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo, palo_activo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo)
    
    return hp_enemigo, jugador_hp, palo_activo

def turno_arquero(jugador, jugador_hp, hp_enemigo, hp_maximo):
    print(f"===== TURNO DE {jugador} (ARQUERO) =====")
    print("Acciones disponibles: Flechas - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Flechas", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    palo_activo = False  # Definir la variable aquí

    if accion == "Flechas":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} tira flechas causando {daño} puntos de daño.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo, palo_activo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo)
    
    return hp_enemigo, jugador_hp, palo_activo

def regenerar_vida(jugadores_hp, vida_inicial):
    print("Regenerando vida de los personajes...")
    for i in range(len(jugadores_hp)):
        jugadores_hp[i] = vida_inicial[i]
    print("¡La vida de todos los personajes ha sido regenerada!")

def ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp, palo_activo):
    if palo_activo:
        print(f"{jugadores[enemigo_index]} lanza el palo y {enemigos[enemigo_index]} se distrae.")
        palo_activo = False
    else:
        enemigo_ataque = random.randint(10, 40)
        jugadores_vivos = [i for i in range(len(jugadores_hp)) if jugadores_hp[i] > 0]

        if not jugadores_vivos:
            print("¡No quedan jugadores con vida!")
        else:
            jugador_atacado_index = random.choice(jugadores_vivos)  # Selecciona un jugador al azar que esté vivo
            jugadores_hp[jugador_atacado_index] -= enemigo_ataque
            jugadores_hp[jugador_atacado_index] = max(0, jugadores_hp[jugador_atacado_index])  # Evitar HP negativo
            print(f"{enemigos[enemigo_index]} ataca a {jugadores[jugador_atacado_index]} y causa {enemigo_ataque} de daño.")
            print(f"{jugadores[jugador_atacado_index]}: {jugadores_hp[jugador_atacado_index]} HP")
    
    return jugadores_hp, palo_activo

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
    palo_activo = False  # Inicializar palo_activo
    
    while enemigo_index < len(enemigos) and sum(jugadores_hp) > 0:
        jugador_actual = jugadores[jugador_index]
        hp_enemigo = enemigos_hp[enemigo_index]
        hp_maximo = [TANQUE_HP, BRUJO_HP, ARQUERO_HP][jugador_index]  # Obtener el HP máximo del jugador actual
        
        # Mostrar el estado actual antes del turno
        mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index)
        
        # Turno del jugador
        if jugador_actual == tanque:
            hp_enemigo, jugadores_hp[jugador_index], palo_activo = turno_tanque(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo)
        elif jugador_actual == brujo:
            hp_enemigo, jugadores_hp[jugador_index], palo_activo = turno_brujo(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo)
        elif jugador_actual == arquero:
            hp_enemigo, jugadores_hp[jugador_index], palo_activo = turno_arquero(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo)
        
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
            jugadores_hp, palo_activo = ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp, palo_activo)
        
        jugador_index = (jugador_index + 1) % len(jugadores)  # Reinicia el turno cuando llega al último jugador
    
    if enemigo_index == len(enemigos) and sum(jugadores_hp) > 0:
        cad1="¡HAS DERROTADO A TODOS LOS ENEMIGOS!"
        cad2=cad1.center(50,"=")
        print(cad2)
        
    else:
        cad1="¡HAS DERROTADO A TODOS LOS ENEMIGOS!"
        cad2=cad1.center(50,"=")
        print(cad2)

if __name__ == "__main__":
    main()
