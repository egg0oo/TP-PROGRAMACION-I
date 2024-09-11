import random
from verificacion import verificarnombre

def tabla(matriz, cf, cc):
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

def establecer_matriz(matriz, jugador_actual, enemigo_index, daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2, tanque, brujo, arquero):
    if jugador_actual==tanque and enemigo_index==0:
        matriz[0][0]=daño_total_tanque
    elif jugador_actual==brujo and enemigo_index==0:
        matriz[1][0]=daño_total_brujo
    elif jugador_actual==arquero and enemigo_index==0:
        matriz[2][0]=daño_total_arquero
    elif jugador_actual==tanque and enemigo_index==1:
        matriz[0][1]=daño_total_tanque1
    elif jugador_actual==brujo and enemigo_index==1:
        matriz[1][1]=daño_total_brujo1
    elif jugador_actual==arquero and enemigo_index==1:
        matriz[2][1]=daño_total_arquero1
    elif jugador_actual==tanque and enemigo_index==2:
        matriz[0][2]=daño_total_tanque2
    elif jugador_actual==brujo and enemigo_index==2:
        matriz[1][2]=daño_total_brujo2
    elif jugador_actual==arquero and enemigo_index==2:
        matriz[2][2]=daño_total_arquero2

def suma_de_daño(jugador_actual, enemigo_index, daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2, daño_tanque, daño_brujo, daño_arquero, tanque, brujo, arquero):
    if jugador_actual==tanque and enemigo_index==0:
            daño_total_tanque+=daño_tanque
    elif jugador_actual==brujo and enemigo_index==0:
            daño_total_brujo +=daño_brujo
    elif jugador_actual==arquero and enemigo_index==0:
            daño_total_arquero+=daño_arquero
    elif jugador_actual==tanque and enemigo_index==1:
            daño_total_tanque1+=daño_tanque
    elif jugador_actual==brujo and enemigo_index==1:
            daño_total_brujo1+=daño_brujo
    elif jugador_actual==arquero and enemigo_index==1:
            daño_total_arquero1 +=daño_arquero
    elif jugador_actual==tanque and enemigo_index==2:
            daño_total_tanque2+=daño_tanque
    elif jugador_actual==brujo and enemigo_index==2:
            daño_total_brujo2+=daño_brujo
    elif jugador_actual==arquero and enemigo_index==2:
            daño_total_arquero2 +=daño_arquero
    return daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2

def ataque():
    daño = random.randint(60, 100) 
    return daño

def magia_negra():
    daño = random.randint(20, 140)
    return daño

def usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados, items):
    print("Items disponibles: ", items)
    item = input("¿Qué ítem usarás?: ").capitalize()
    
    if item == "Vendaje":
        if not items_usados[0]:
            jugador_hp += 60
            print(f"{jugador} usa Vendaje y recupera 60 puntos de HP.")
            items_usados[0] = True
        else:
            print("El Vendaje ya ha sido usado y no se puede usar nuevamente.")
        items[0:1]=[]
    
    elif item == "Poción":
        if not items_usados[1]:
            jugador_hp += 100
            print(f"{jugador} usa Poción y recupera 100 puntos de HP.")
            items_usados[1] = True
        else:
            print("La Poción ya ha sido usada y no se puede usar nuevamente.")
        items[1:len(items)-1]=[]
    
    elif item == "Palo":
        if not items_usados[2]:
            daño = 40
            hp_enemigo -= daño
            print(f"{jugador} arroja el Palo y le pega al enemigo, causandole {daño} puntos de daño.")
            items_usados[2] = True
        else:
            print("El Palo ya ha sido usado y no se puede usar nuevamente.")
        items[1:len(items)]=[]
    
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

def turno_tanque(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados, daño, items):
    print(f"===== TURNO DE {jugador} (TANQUE) =====")
    print("Acciones disponibles: Atacar - Bloquear - Items")
    accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    while accion not in ["Atacar", "Bloquear", "Items"]:
        print("Acción inválida.")
        accion = input(f"¿Qué hará {jugador}? ").capitalize()
    
    bloqueo_exitoso = False
    
    if accion == "Atacar":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{jugador} ataca causando {daño} puntos de daño.")
    
    elif accion == "Bloquear":
        bloqueo_exitoso = bloquear(jugadores, jugadores_hp)
    
    elif accion == "Items":
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados, items)
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso, daño

def turno_brujo(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores_hp, items_usados, daño, items):
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
        daño = magia_negra()
        hp_enemigo -= daño
        print(f"{jugador} usa un hechizo de magia negra causando {daño} puntos de daño.")
    
    elif accion == "Items":
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo, items_usados, items)
    
    bloqueo_exitoso = False
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso, daño

def turno_arquero(jugador, jugador_hp, hp_enemigo, hp_maximo, jugadores_hp, items_usados,daño, items):
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
        jugador_hp, hp_enemigo = usar_item(jugador, jugador_hp, hp_enemigo, hp_maximo,items_usados, items)
    
    bloqueo_exitoso = False
    
    return hp_enemigo, jugador_hp, jugadores_hp, bloqueo_exitoso, daño

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
    enemigo_ataque = random.randint(20, 50)
    
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
    print()
    print("Nombra a tus personajes. Solo se permiten caracteres alfabéticos.")
    tanque, brujo, arquero = verificarnombre()

    print(f"Tus personajes son {tanque}, {brujo} y {arquero}")
    
    TANQUE_HP = 350
    BRUJO_HP = 250
    ARQUERO_HP = 200
    jugadores = [tanque, brujo, arquero]
    jugadores_hp = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]
    vida_inicial = [TANQUE_HP, BRUJO_HP, ARQUERO_HP]

    enemigos = ["Enemigo 1", "Enemigo 2", "Enemigo 3"]
    enemigos_hp = [400, 500, 600]
    enemigo_index = 0
    
    matriz=[[0]*len(enemigos) for i in range(len(jugadores))]
    
    items=["Vendaje","Poción","Palo"]
    items_usados = [False, False, False]  # Vendaje, Poción, Palo
    
    print(f"¡Se acerca {enemigos[enemigo_index]} con {enemigos_hp[enemigo_index]} HP!")
    
    jugador_index = 0
    
    daño = 0
    daño_tanque = 0
    daño_brujo = 0
    daño_arquero = 0
    daño_total_tanque=0
    daño_total_brujo=0
    daño_total_arquero=0
    daño_total_tanque1=0
    daño_total_brujo1=0
    daño_total_arquero1=0
    daño_total_tanque2=0
    daño_total_brujo2=0
    daño_total_arquero2=0
    
    while enemigo_index < len(enemigos) and sum(jugadores_hp) > 0:
        jugador_actual = jugadores[jugador_index]
        hp_enemigo = enemigos_hp[enemigo_index]
        hp_maximo = [TANQUE_HP, BRUJO_HP, ARQUERO_HP][jugador_index]
        
        mostrar_estado(jugadores, jugadores_hp, enemigos, enemigos_hp, enemigo_index)
        
        if jugador_actual == tanque:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso, daño_tanque = turno_tanque(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores, jugadores_hp, items_usados, daño,items)
        elif jugador_actual == brujo:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso, daño_brujo = turno_brujo(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores_hp, items_usados, daño,items)
        elif jugador_actual == arquero:
            hp_enemigo, jugadores_hp[jugador_index], jugadores_hp, bloqueo_exitoso, daño_arquero = turno_arquero(jugador_actual, jugadores_hp[jugador_index], hp_enemigo, hp_maximo, jugadores_hp, items_usados, daño,items)
        
        enemigos_hp[enemigo_index] = hp_enemigo
        
        daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2=suma_de_daño(jugador_actual, enemigo_index, daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2, daño_tanque, daño_brujo, daño_arquero, tanque, brujo, arquero)
        
        establecer_matriz(matriz, jugador_actual, enemigo_index, daño_total_tanque, daño_total_brujo, daño_total_arquero, daño_total_tanque1, daño_total_brujo1, daño_total_arquero1,  daño_total_tanque2, daño_total_brujo2, daño_total_arquero2, tanque, brujo, arquero)
        
        if hp_enemigo <= 0:
            print(f"¡{enemigos[enemigo_index]} ha sido derrotado!")
            enemigo_index += 1
            print()
            if enemigo_index == 1:
                print("Matarme no cambiará nada, forastero. La maldición ya corre por tus venas, como lo hizo con nosotros. Caerás igual que los que te precedieron.")
                print()
            elif enemigo_index == 2:
                print("Has luchado bien, pero incluso si logras destruirme, no serás más que una sombra, como lo es este imperio. La oscuridad de Aeldenor ya ha reclamado tu alma, y yo seré el testigo de tu caída.")
                print()
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
    
    print()
    print(f"Jugador 1= {tanque}, jugador 2= {brujo} y jugador 3= {arquero} ")
    tabla(matriz, len(jugadores), len(enemigos))
    print()
if __name__ == "__main__":
    main()
