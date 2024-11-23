import random
from verificacion import nombrar
from estado import mostrar_estado

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
                "muerte":0,
                "turnos":0,
                }
        file.close()
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
            ataquemin = int(datos[2])
            ataquemax = int(datos[3])
            enemigos[enemigo] = {
                "vida": vida,
                "ataquemin": ataquemin,
                "ataquemax": ataquemax,
            }
        file.close()
        return enemigos

def crear_archivos(personajes):
    l=list(personajes["TANQUE"].keys())
    for i in range(2):
        del personajes["TANQUE"][l[i+1]]
        del personajes["BRUJO"][l[i+1]]
        del personajes["ARQUERO"][l[i+1]]
    l=list(personajes["TANQUE"].keys())
    for stats in l:
        if stats == "daño total":
            for i in range(len(personajes['TANQUE'][stats])):
                try:
                    
                    arch = open(f"{stats.lower()} enemigo {i}.csv", "wt")
                except IOError:
                    print(f"No se pudo crear el archivo para {stats}")
                else:
                    arch.write("TANQUE;"+str(personajes['TANQUE'][stats][i])+"\n")
                    arch.write("BRUJO;"+str(personajes['BRUJO'][stats][i])+"\n")
                    arch.write("ARQUERO;"+str(personajes['ARQUERO'][stats][i])+"\n")
                    arch.close()
            continue
        try:
            arch = open(f"{stats.lower()}.csv", "wt")
        except IOError:
            print(f"No se pudo crear el archivo para {stats}")
        else:
            
            arch.write("TANQUE;"+str(personajes['TANQUE'][stats])+"\n")
            arch.write("BRUJO;"+str(personajes['BRUJO'][stats])+"\n")
            arch.write("ARQUERO;"+str(personajes['ARQUERO'][stats])+"\n")
            arch.close()
                
def usar_item(nombre, personaje, hp_enemigo, items_usados, items, numeros):
    print("Items disponibles: ", items)
    
    while True:
        try:
            item = input("¿Qué ítem usarás? o presiona alguna tecla si no tienes más items: ").strip().upper()
            if item == "VENDAJE":
                if items_usados[0] == 1:  
                    raise ValueError("El Vendaje ya ha sido usado y no se puede usar nuevamente.")
                personaje['vida'] += 70
                print(f"{nombre} usa Vendaje y recupera 60 puntos de HP.")
                items_usados[0] == 1  
                items.remove("Vendaje")
                personaje['Items']+=1
                break  
            elif item == "POCIÓN" or item== "POCION":
                if items_usados[1] == 1:
                    raise ValueError("La Poción ya ha sido usado y no se puede usar nuevamente.")                    
                personaje['vida']+= 120
                print(f"{nombre} usa Poción y recupera 100 puntos de HP.")
                items.remove("Poción")
                items_usados[1]=1
                personaje['Items']+=1                
                break  
            elif item == "PALO":
                if items_usados[2]==1:
                    raise ValueError("El Palo ya ha sido usado y no se puede usar nuevamente.")
                daño = 85
                daño=min(daño,hp_enemigo)
                hp_enemigo -= daño
                personaje['daño total'][numeros] += daño
                print(f"{nombre} arroja el Palo y le pega al enemigo, causandole {daño} puntos de daño.")
                items.remove("Palo")
                items_usados[2]=1
                personaje['Items']+=1
                break
            elif items == []:
                print("No quedan más items")
                break
            else:
                print("Ítem no válido.")
        except (IndexError, ValueError) as msg:
            print(msg)
                    
    jugador_hp = min(personaje['vida'], personaje['vidamax'])
    return jugador_hp, hp_enemigo

def atacar(enemigo, numero, PERSONAJE):
    daño = random.randint(70, 110)
    daño = min(daño, enemigo['vida'])
    enemigo['vida'] -= daño
    PERSONAJE['daño total'][numero] += daño
    return daño

def bloquear():
    resultado_bloqueo = random.randint(1, 2) == 1
    
    if resultado_bloqueo:
        print("¡El bloqueo ha sido un éxito total! Ningún jugador recibe daño este turno.")
    else:
        print("¡El bloqueo ha fallado!")
    return resultado_bloqueo
    
def turno_tanque(TANQUE, daño, enemigos, nombre, items, items_usados, resultado_bloqueo, numero):
    if TANQUE["vida"] > 0:
        TANQUE['turnos'] += 1
        print(f"===== TURNO DE {nombre} (TANQUE) =====")
        accion = input("Acciones disponibles: Atacar - Bloquear - Items\n").strip().upper()
        while accion not in TANQUE["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "ATACAR":
            daño = atacar(enemigos, numero, TANQUE)
            print(f"{nombre} ataca causando {daño} puntos de daño.")
        elif accion == "BLOQUEAR":
            resultado_bloqueo = bloquear()  
        else:
            TANQUE['vida'], enemigos['vida'] = usar_item(nombre, TANQUE, enemigos['vida'], items_usados, items, numero)
    else:
        print(f"{nombre} está muerto, no puede actuar.")
        TANQUE['muerte']==1
    return resultado_bloqueo

def turno_brujo(BRUJO, daño, enemigos, nombre, items, items_usados, numero):
    if BRUJO["vida"] > 0:
        BRUJO['turnos'] += 1
        print(f"===== TURNO DE {nombre} (BRUJO) =====")
        accion = input("Acciones disponibles: Bola de fuego - Magia negra - Items\n").strip().upper()
        while accion not in BRUJO["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "BOLA DE FUEGO":
            daño = atacar(enemigos, numero, BRUJO)
            print(f"{nombre} usa bola de fuego causando {daño} puntos de daño.")
        elif accion == "MAGIA NEGRA":
            daño = random.randint(50, 150)
            daño = min(daño, enemigos['vida'])
            enemigos['vida'] -= daño
            BRUJO['daño total'][numero] += daño
            print(f"{nombre} usa un hechizo de magia negra causando {daño} puntos de daño.")  
        else:
            BRUJO['vida'], enemigos['vida'] = usar_item(nombre, BRUJO, enemigos['vida'], items_usados, items, numero)  
    else:
        print(f"{nombre} está muerto, no puede actuar.")
        BRUJO['muerte']==1

def turno_arquero(ARQUERO, daño, enemigos, nombre, items, items_usados, numero):
    if ARQUERO["vida"] > 0:
        ARQUERO['turnos'] += 1
        print(f"===== TURNO DE {nombre} (ARQUERO) =====")
        accion = input("Acciones disponibles: Tirar flechas - Items\n").strip().upper()
        while accion not in ARQUERO["acciones"]:
            accion = input("Acción no válida. Intenta de nuevo.\n").strip().upper()
        
        if accion == "TIRAR FLECHAS":
            daño = atacar(enemigos, numero, ARQUERO)
            print(f"{nombre} tira flechas causando {daño} puntos de daño.")
        else:
            ARQUERO['vida'], enemigos['vida'] = usar_item(nombre, ARQUERO, enemigos['vida'], items_usados, items, numero)  
    else:
        print(f"{nombre} está muerto, no puede actuar.")
        ARQUERO['muerte']==1

def muerte(personajes, enemigos):
    jugadores_vivos = {}
    for nombre in personajes:
        if personajes[nombre]['vida'] > 0:
            jugadores_vivos[nombre] = personajes[nombre]
        else:
            personajes[nombre]['muerte'] = 1

    if not jugadores_vivos:
        print("¡No quedan jugadores con vida!")
    return jugadores_vivos

def ataque_enemigo(ENEMIGO, personajes, resultado_bloqueo, nombres, enemigo_actual, jugadores_vivos):
    if not resultado_bloqueo:
        jugador_atacado = random.choice(list(jugadores_vivos))
        daño=random.randint(ENEMIGO['ataquemin'], ENEMIGO['ataquemax'])
        personajes[jugador_atacado]['vida'] -= daño
        personajes[jugador_atacado]['vida'] = max(0, personajes[jugador_atacado]['vida'])
        
        print(f"{enemigo_actual} ataca a {nombres[jugador_atacado]} y causa {daño} de daño.")
        print(f"{nombres[jugador_atacado]}: {personajes[jugador_atacado]['vida']} HP")

def cambio_enemigo(enemigos, enemigo_actual, numero_enemigo):
    if enemigos[enemigo_actual]['vida'] <= 0: 
        print(f"{enemigo_actual} ha sido derrotado.")
        numero_enemigo += 1
        if numero_enemigo == 1:
            print()
            print("Matarme no cambiará nada, forastero. La maldición ya corre por tus venas, como lo hizo con nosotros. Caerás igual que los que te precedieron.")
            enemigo_actual = list(enemigos)[numero_enemigo]
        elif numero_enemigo == 2:
            print()
            print("Has luchado bien, pero incluso si logras destruirme, no serás más que una sombra, como lo es este imperio. La oscuridad de Aeldenor ya ha reclamado tu alma, y yo seré el testigo de tu caída.")
            enemigo_actual = list(enemigos)[numero_enemigo]
        else:
            numero_enemigo = 2
    return enemigo_actual, numero_enemigo

def finalizacion(personajes, enemigos):
    if personajes['TANQUE']['vida'] == 0 and personajes['BRUJO']['vida'] == 0 and personajes['ARQUERO']['vida'] == 0:
        print()
        print("Has sido derrotado!!!. Inicia de vuelta el programa e inténtalo de nuevo.")
        return True    
    if enemigos['ENEMIGO_Z']['vida'] <= 0:
        print()
        print("¡Todos los enemigos han sido derrotados!")
        print("Has ganado!!! Felicidades.")
        return True
    return False

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
    
    daño = 0
    numero_enemigo = 0  # Índice del enemigo actual
    enemigo_actual = list(enemigos)[numero_enemigo]
    resultado_bloqueo=False
    mostrar_estado(personajes, enemigos, enemigo_actual)
    jugadores_vivos=personajes.copy()
    print("En el combate el tanque y el brujo tienen 3 opciones: el ataque normal, una habilidad y los items pero se agotan al usarlos")
    print("El arquero solamente puede hacer daño con sus flechas y usar los items")
    print("Los items que utiliza el equipo son: Vendaje (recupera 70 de vida), Poción (recupera 120 de vida) y palo (inflige 85 puntos de daño)")
    print()

    while True:
        resultado_bloqueo = turno_tanque(personajes['TANQUE'], daño, enemigos[enemigo_actual], nombres['TANQUE'], items, items_usados, resultado_bloqueo, numero_enemigo)
            
        if enemigos[enemigo_actual]['vida'] > 0:
            ataque_enemigo(enemigos[enemigo_actual], personajes, resultado_bloqueo, nombres, enemigo_actual, jugadores_vivos)

        resultado_bloqueo = False
         
        jugadores_vivos=muerte(personajes,enemigos)
        
        enemigo_actual, numero_enemigo = cambio_enemigo(enemigos, enemigo_actual, numero_enemigo)
            
        mostrar_estado(personajes, enemigos, enemigo_actual)
            
        if finalizacion(personajes,enemigos):
            break
            
        turno_brujo(personajes['BRUJO'], daño, enemigos[enemigo_actual], nombres['BRUJO'], items, items_usados, numero_enemigo)

        if enemigos[enemigo_actual]['vida'] > 0:
            ataque_enemigo(enemigos[enemigo_actual], personajes, resultado_bloqueo, nombres, enemigo_actual, jugadores_vivos)
        
        jugadores_vivos=muerte(personajes,enemigos)
        
        enemigo_actual, numero_enemigo = cambio_enemigo(enemigos, enemigo_actual, numero_enemigo)

        mostrar_estado(personajes, enemigos, enemigo_actual)
            
        if finalizacion(personajes,enemigos):
            break
            
        turno_arquero(personajes['ARQUERO'], daño, enemigos[enemigo_actual], nombres['ARQUERO'], items, items_usados, numero_enemigo)
            
        if enemigos[enemigo_actual]['vida'] > 0:
            ataque_enemigo(enemigos[enemigo_actual], personajes, resultado_bloqueo, nombres, enemigo_actual, jugadores_vivos)
            
        enemigo_actual, numero_enemigo = cambio_enemigo(enemigos, enemigo_actual, numero_enemigo)
        
        mostrar_estado(personajes, enemigos, enemigo_actual)
        
        jugadores_vivos=muerte(personajes,enemigos)
        
        if finalizacion(personajes,enemigos):
            break
    
    crear_archivos(personajes)

if __name__ == "__main__":
    main()