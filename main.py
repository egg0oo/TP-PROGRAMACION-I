import random

#No tiene incorporado los modulos
#hay que hacer el contador de daño correcto
#revisar si los turnos estan correctos
#hacer los archivos de salida q agrupen los datos
#establecer el tema de la lista de items, items usados
#incorporar las funciones de regenerar vida
#Hacer todo el sistema de combate que progresa entre los enemigos
#Lo q esta en la funcion de ataque q involucra las funciones de atacar y seleccionar enemigos no las borre porque maybe nos pueden ayudar mas adelante pero son borrables

def nombrar(personaje):
    nombre = input("Ingresa el nombre: ").upper()
    if verificar(nombre):
        return nombre
    else:
        print("El nombre es inválido. Intente nuevamente.")
        return nombrar(personaje)

def verificar(nombre):
    return nombre.isalpha()

def cargar_stats(archivo):
    try:
        personajes = {}
        file = open(archivo, "r")
    except IOError:
        print("No se pudo abrir el archivo")
    else:
        for linea in file:
            datos = linea.strip().split(";")
            personaje = datos[0]
            vida = int(datos[1])
            acciones = datos[2:]
            personajes[personaje] = {
                "vida":vida,
                "vidamax":vida,
                "acciones":acciones,
                "daño total":[0,0,0],
                "Items":0,
                "muertes":0,
                "turnos":0,
                }
        linea = file.readline()
        file.close
        return personajes
    

def cargar_stats_enemigos(archivo):
    try:
        enemigos = {}
        file = open(archivo, "r")
    except IOError:
        print("No se pudo abrir el archivo")
    else:
        for linea in file:
            datos = linea.strip().split(";")
            enemigo = datos[0]
            vida = int(datos[1])
            ataque = int(datos[2])
            enemigos[enemigo] = {
                "vida": vida,
                "ataque": ataque,
            }
        file.close()
        return enemigos

def usar_item(nombre, jugador_hp, hp_enemigo, hp_maximo, items_usados, items):
    print("Items disponibles: ", items)
    
    while True:
        try:
            item = input("¿Qué ítem usarás? o presiona alguna tecla si no tienes más items: ").strip().upper()
            if item == "VENDAJE":
                if items_usados[0] == 1:  
                    raise ValueError("El Vendaje ya ha sido usado y no se puede usar nuevamente.")
                jugador_hp += 60
                print(f"{nombre} usa Vendaje y recupera 60 puntos de HP.")
                items_usados[0] == 1  
                items.remove("Vendaje")  
                break  
            elif item == "POCIÓN" or item== "POCION":
                if items_usados[1] == 1:
                    raise ValueError("La Poción ya ha sido usado y no se puede usar nuevamente.")                    
                jugador_hp += 100
                print(f"{nombre} usa Poción y recupera 100 puntos de HP.")
                items.remove("Poción")
                items_usados[1]=1
                break  
            elif item == "PALO":
                if items_usados[2]==1:
                    raise ValueError("El Palo ya ha sido usado y no se puede usar nuevamente.")                    
                daño = 40
                hp_enemigo -= daño
                print(f"{nombre} arroja el Palo y le pega al enemigo, causandole {daño} puntos de daño.")
                items.remove("Palo")
                items_usados[2]=1
                break      
            elif items == []:
                print("No quedan más items")
                break
            else:
                print("Ítem no válido.")
        except (IndexError, ValueError) as msg:
            print(msg)
                    
    jugador_hp = min(jugador_hp, hp_maximo)
    return jugador_hp, hp_enemigo

def bloquear():
    resultado_bloqueo = random.randint(1, 2) == 1
    
    if resultado_bloqueo:
        print("¡El bloqueo ha sido un éxito total! Ningún jugador recibe daño este turno.")
    else:
        print("¡El bloqueo ha fallado!")
    
    return resultado_bloqueo

def mostrar_estado(personajes, enemigos, numero_enemigo):
    print("\nEstado actual:")
    
    for nombre in personajes:
        print(f"{nombre}: {personajes[nombre]['vida']} HP")
   
    enemigo_actual = list(enemigos)[numero_enemigo]
    print(f"{enemigo_actual}: {enemigos[enemigo_actual]['vida']} HP\n")

def turno_tanque(TANQUE, daño, enemigos, nombre, items, items_usados,resultado_bloqueo):
    if TANQUE["vida"] > 0:
        print(f"===== TURNO DE {nombre} (TANQUE) =====")
        accion = input("Acciones disponibles: Atacar - Bloquear - Items\n").strip().upper()
        while accion not in TANQUE["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "ATACAR":
            daño = random.randint(60, 100)
            enemigos['vida'] -= daño
            print(f"{nombre} ataca causando {daño} puntos de daño.")

        elif accion == "BLOQUEAR":
            resultado_bloqueo = bloquear()  
        else:
            TANQUE['vida'], enemigos['vida'] = usar_item(nombre, TANQUE['vida'], enemigos['vida'], 350, items_usados, items)  
    else:
        print(f"{nombre} está muerto, no puede actuar.")
    return resultado_bloqueo

def turno_brujo(BRUJO, daño, enemigos, nombre, items, items_usados):
    if BRUJO["vida"] > 0:
        print(f"===== TURNO DE {nombre} (BRUJO) =====")
        accion = input("Acciones disponibles: Bola de fuego - Magia negra - Items\n").strip().upper()
        while accion not in BRUJO["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "BOLA DE FUEGO":
            daño = random.randint(60, 100)
            enemigos['vida'] -= daño
            print(f"{nombre} ataca causando {daño} puntos de daño.")

        elif accion == "MAGIA NEGRA":
            daño = random.randint(40, 120)
            enemigos['vida'] -= daño
            print(f"{nombre} ataca causando {daño} puntos de daño.")  
        else:
            BRUJO['vida'], enemigos['vida'] = usar_item(nombre, BRUJO['vida'], enemigos['vida'], 350, items_usados, items)  
    else:
        print(f"{nombre} está muerto, no puede actuar.")

def turno_arquero(ARQUERO, daño, enemigos, nombre, items, items_usados):
    if ARQUERO["vida"] > 0:
        print(f"===== TURNO DE {nombre} (ARQUERO) =====")
        accion = input("Acciones disponibles: Tirar flechas - Items\n").strip().upper()
        while accion not in ARQUERO["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "TIRAR FLECHAS":
            daño = random.randint(60, 100)
            enemigos['vida'] -= daño
            print(f"{nombre} ataca causando {daño} puntos de daño.")
        else:
            ARQUERO['vida'], enemigos['vida'] = usar_item(nombre, ARQUERO['vida'], enemigos['vida'], 350, items_usados, items)  
    else:
        print(f"{nombre} está muerto, no puede actuar.")

def ataque_enemigo(ENEMIGO, personajes, resultado_bloqueo, nombres, numero_enemigo):
    enemigo_ataque = random.randint(20, 50)
    enemigos_nombre = list(ENEMIGO.keys())
    enemigo_actual = enemigos_nombre[numero_enemigo]

    jugadores_vivos = {}
    for nombre in personajes:
        if personajes[nombre]['vida'] > 0:
            jugadores_vivos[nombre] = personajes[nombre]

    if not jugadores_vivos:
        print("¡No quedan jugadores con vida!")
        return

    if not resultado_bloqueo:
        resultado_bloqueo = False
        jugador_atacado = random.choice(list(jugadores_vivos.keys()))
        personajes[jugador_atacado]['vida'] -= enemigo_ataque
        personajes[jugador_atacado]['vida'] = max(0, personajes[jugador_atacado]['vida'])
        
        print(f"{enemigo_actual} ataca a {nombres[jugador_atacado]} y causa {enemigo_ataque} de daño.")
        print(f"{nombres[jugador_atacado]}: {personajes[jugador_atacado]['vida']} HP")

def main():
    cad = "EL LEGADO PERDIDO".center(29, "=")
    print(cad)
    
    print("En las sombras de un imperio muerto, susurran los ecos de un poder olvidado.")
    print("Aeldenor, se encuentra en ruinas, consumido por una maldición.")
    print("Los descendientes de los corrompidos, herederos de una tragedia ancestral, buscan respuestas en un mundo que ha olvidado su propia condena.")
    print("Al enfrentarse a los enemigos irás descubriendo más de la historia de Aeldenor y el secreto que conlleva la maldición.")
    print()
    
    print("Nombra a tus personajes. Solo se permiten caracteres alfabéticos.")
    
    tanque = nombrar("TANQUE")
    print(f"El nombre de tu TANQUE es {tanque}")
    brujo = nombrar("BRUJO")
    print(f"El nombre de tu BRUJO es {brujo}")
    arquero = nombrar("ARQUERO")
    print(f"El nombre de tu ARQUERO es {arquero}")
    
    nombres = {
        "TANQUE": tanque,
        "BRUJO": brujo,
        "ARQUERO": arquero
    }
    
    items = ["Vendaje", "Poción", "Palo"]
    items_usados = [0, 0, 0]  # Vendaje, Poción, Palo
    
    personajes = cargar_stats("stats.text")
    enemigos = cargar_stats_enemigos("stats_enemigos.text")
    
    print(personajes)
    
    daño = 0
    numero_enemigo = 0  # Indice del enemigo actual

    while numero_enemigo < len(enemigos):
        enemigo_actual = list(enemigos.keys())[numero_enemigo]
        
        if enemigos[enemigo_actual]['vida'] <= 0: # 1* PONER TODO ESTE IF ELSE EN UNA FUNCION
            print(f"{enemigo_actual} ha sido derrotado.")
            numero_enemigo += 1
            continuar = False  # El enemigo ha sido derrotado
        else:
            continuar = True

        if continuar:
            resultado_bloqueo=False
            mostrar_estado(personajes, enemigos, numero_enemigo)
            resultado_bloqueo=turno_tanque(personajes['TANQUE'], daño, enemigos[enemigo_actual], nombres['TANQUE'], items, items_usados,resultado_bloqueo)
            
            if enemigos[enemigo_actual]['vida'] > 0:
                ataque_enemigo(enemigos, personajes, resultado_bloqueo, nombres, numero_enemigo)
            resultado_bloqueo=False
            
            mostrar_estado(personajes, enemigos, numero_enemigo)
            turno_brujo(personajes['BRUJO'], daño, enemigos[enemigo_actual], nombres['BRUJO'], items, items_usados)

            if enemigos[enemigo_actual]['vida'] > 0:
                ataque_enemigo(enemigos, personajes, resultado_bloqueo, nombres, numero_enemigo)

            if enemigos[enemigo_actual]['vida'] <= 0: # 1* PONER TODO ESTE IF ELSE EN UNA FUNCION
                print(f"{enemigo_actual} ha sido derrotado.")
                numero_enemigo += 1
                continuar = False
            else:
                continuar = True

        if continuar:
            mostrar_estado(personajes, enemigos, numero_enemigo)
            turno_arquero(personajes['ARQUERO'], daño, enemigos[enemigo_actual], nombres['ARQUERO'], items, items_usados)
            
            if enemigos[enemigo_actual]['vida'] > 0:
                ataque_enemigo(enemigos, personajes, resultado_bloqueo, nombres, numero_enemigo)

            if enemigos[enemigo_actual]['vida'] <= 0:
                print(f"{enemigo_actual} ha sido derrotado.")
                numero_enemigo += 1

    print("¡Todos los enemigos han sido derrotados!")

if __name__ == "__main__":
    main()