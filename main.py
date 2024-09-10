import random
from verificacion import verificarnombre

def listardeudor(matriz, cf, cc):
    print("                            ")
    print("Personajes/enemigos", end="")
    for i in range(1, cc+1):
        print("%7d" % (i), end=" ")
    print()
    
    for i in range(cf):
        texto = "Personaje " + str(i+1) + "        "
        print("%7s" % (texto), end="")
        for j in range(cc):
            print("%7s" % (matriz[i][j]), end=" ")
        print()

def InicializarMatriz(matriz, cf, cc):
    for i in range(cf):
        matriz.append([])
        for j in range(cc):
            matriz[i].append('x')

def ataque():
    daño = random.randint(60, 100)
    return daño

def usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados):
    print("Items disponibles: Vendaje (60 HP), Poción (100 HP), Palo (-40 HP enemigo)")
    item = input("¿Qué ítem usarás?: ").capitalize()
    
    if item == "Vendaje":
        if not items_usados[0]:
            jugador_hp += 60
            print(f"{jugador} usa Vendaje y recupera 60 puntos de HP.")
            items_usados[0] = True
        else:
            print("El Vendaje ya ha sido usado y no se puede usar nuevamente.")
    
    elif item == "Poción":
        if not items_usados[1]:
            jugador_hp += 100
            print(f"{jugador} usa Poción y recupera 100 puntos de HP.")
            items_usados[1] = True
        else:
            print("La Poción ya ha sido usada y no se puede usar nuevamente.")
    
    elif item == "Palo":
        if not items_usados[2]:
            daño = 40
            hp_enemigo -= daño
            print(f"{jugador} arroja el Palo y le pega al enemigo, causandole {daño} puntos de daño.")
            items_usados[2] = True
        else:
            print("El Palo ya ha sido usado y no se puede usar nuevamente.")
    
    else:
        print("Ítem no válido.")
    
    jugador_hp = min(jugador_hp, hp_maximo)
    return jugador_hp, hp_enemigo

def bloquear(jugadores, jugadores_hp):
    resultado_bloqueo = random.randint(1, 2) == 2
    
    if resultado_bloqueo == 1:
        print("¡El bloqueo ha sido un éxito total! Ningún jugador recibe daño este turno.")
    else:
        print("¡El bloqueo ha fallado!")
    
    return resultado_bloqueo

def turno_tanque(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados):
    print(f"===== TURNO DE {jugador} (TANQUE) =====")
    print("Acciones disponibles: Atacar - Bloquear - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Atacar", "Bloquear", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").Capitalize()
    
    bloqueo_exitoso = False
    
    if accion == "Atacar":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} ataca causando {daño} puntos de daño.")
    
    elif accion == "Bloquear":
        bloqueo_exitoso = bloquear(jugadores, jugadores_hp)
    
    elif accion == "Items":
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados)
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso

def turno_brujo(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados):
    print(f"===== TURNO DE {jugador} (BRUJO) =====")
    print("Acciones disponibles: Bola de fuego - Magia negra - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Bola de fuego", "Magia negra", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    if accion == "Bola de fuego":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} usa bola de fuego causando {daño} puntos de daño.")
    
    elif accion == "Magia negra":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} usa un hechizo de magia negra causando {daño} puntos de daño.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados)
    
    bloqueo_exitoso = False
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso

def turno_arquero(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados):
    print(f"===== TURNO DE {jugador} (ARQUERO) =====")
    print("Acciones disponibles: Flechas - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Flechas", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    if accion == "Flechas":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} tira flechas causando {daño} puntos de daño.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados)
    
    bloqueo_exitoso = False
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso

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

def ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp, bloqueo_exitoso):
    enemigo_ataque = random.randint(10, 40)
    
    jugadores_vivos = [i for i in range(len(jugadores_hp)) if jugadores_hp[i] > 0]

    if not jugadores_vivos:
        print("¡No quedan jugadores con vida!")
        return jugadores_hp

    if not bloqueo_exitoso:
        jugador_atacado_index = random.choice(jugadores_vivos)
        jugadores_hp[jugador_atacado_index] -= enemigo_ataque
        jugadores_hp[jugador_atacado_index] = max(0, jugadores_hp[jugador_atacado_index])
    
        print(f"{enemigos[enemigo_index]} ataca a {jugadores[jugador_atacado_index]} y causa {enemigo_ataque} de daño.")
        print(f"{jugadores[jugador_atacado_index]}: {jugadores_hp[jugador_atacado_index]} HP")
    
    return jugadores_hp

def main():
    cad1 = "EL LEGADO PERDIDO"
    cad2 = cad1.center(29, "=")
    print(cad2)
    
    print("En las sombras de un imperio muerto, susurran los ecos de un poder olvidado.")
    print("Aeldenor, se encuentra en ruinas, consumido por una maldición.")
    print("Los descendientes de los corrompidos, herederos de una tragedia ancestral, buscan respuestas en un mundo que ha olvidado su propia condena.")
    print("Al enfrentarse a los enemigos irás descubriendo más de la historia de Aeldenor y el secreto que conlleva la maldición.")
    
    print("Nombra a tus personajes. Solo se permiten caracteres alfabéticos.")
    tanque, brujo, arquero = verificarnombre()

    print(f"Tus personajes son {tanque}, {brujo} y {arquero}", sep="")
    
    TANQUE_HP = 350
    BRUJO_HP = 250
    ARQUERO_HP = 200
    jugadores = [tanque, brujo, arquero]
    jugadores_hp = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]
    vida_inicial = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]

    enemigos = ["Enemigo 1", "Enemigo 2", "Enemigo 3"]
    enemigos_hp = [400, 450, 600]
    enemigo_index = 0
    
    items_usados = [False, False, False]  # Vendaje, Poción, Palo
    
    print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
    
    jugador_index = 0
    
    while enemigo_index < len(enemigos) and sum(jugadores_hp) > 0:
        jugador_actual = jugadores[jugador_index]
        hp_enemigo = enemigos_hp[enemigo_index]
        hp_maximo = [TANQUE_HP, BRUJO_HP, ARQUERO_HP][jugador_index]
        
        mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index)
        
        if jugador_actual == tanque:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso = turno_tanque(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados)
        elif jugador_actual == brujo:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso = turno_brujo(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados)
        elif jugador_actual == arquero:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso = turno_arquero(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados)
        
        enemigos_hp[enemigo_index] = hp_enemigo
        
        if hp_enemigo <= 0:
            print(f"¡{enemigos[enemigo_index]} ha sido derrotado!")
            enemigo_index += 1
            if enemigo_index < len(enemigos):
                print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
            regenerar_vida(jugadores_hp, vida_inicial)
            
        if enemigo_index < len(enemigos):
            jugadores_hp = ataque_enemigo(enemigos, enemigo_index, jugadores, jugadores_hp, bloqueo_exitoso)        

        jugador_index = (jugador_index + 1) % len(jugadores)
    
    if enemigo_index == len(enemigos) and sum(jugadores_hp) > 0:
        cad1 = "¡HAS DERROTADO A TODOS LOS ENEMIGOS!"
        cad2 = cad1.center(50, "=")
        print(cad2)
    else:
        cad1 = "¡HAS PERDIDO ANTE LOS ENEMIGOS!"
        cad2 = cad1.center(50, "=")
        print(cad2)

if __name__ == "__main__":
    main()