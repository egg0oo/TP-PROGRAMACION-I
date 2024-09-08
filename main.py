# JUEGO DE ROL: EL LEGADO PERDIDO

import random

def verificar_nombre(nombre):
    while not (nombre.isalpha()):
        print("El nombre debe estar únicamente compuesto por letras.")
        nombre = input("Intenta nuevamente: ")
    nombre = nombre.upper()
    
    return nombre

def ataque():
    daño = random.randint(40, 80)
    return daño

def turno_tanque(tanque): #REVISAR!
    print(f"TURNO DE {tanque}")
    print("Atacar - Bloquear - Items")
    accion = input(f"Qué hará {tanque}?:").capitalize()
    while accion not in ["Atacar", "Bloquear", "Items"]:
        print("Acción inválida. Elige entre Atacar, Bloquear o Items.")
        accion = input(f"Qué hará {tanque}?: ").capitalize()
    
    if accion == "Atacar":
        daño = ataque()
        hp_enemigo -= daño
        print(f"{tanque} ataca causando {daño} puntos de daño.")
        
    elif accion == "Bloquear":
        print(f"{tanque} bloquea el ataque.")
        
    elif accion == "Items":
        print("Items disponibles: Vendaje (50 HP), Poción (80 HP), Palo Distractor (-20 HP enemigo)")
        item = input("Qué ítem usarás?: ").capitalize()
        if item == "Vendaje":
            TANQUE_HP += 50
            print(f"{tanque} usa Vendaje y recupera 50 puntos de HP.")
        elif item == "Poción":
            TANQUE_HP += 80
            print(f"{tanque} usa Poción y recupera 80 puntos de HP.")
        elif item == "Palo distractor":
            daño = 20
            ENEMIGO_HP -= daño
            print(f"{tanque} usa el Palo Distractor y causa {daño} puntos de daño al enemigo.")
        else:
            print("Ítem no válido.")
    
def main():
    print("Nombra a tus personajes. Solo se permiten caracteres alfabeticos.")
    n = input("TANQUE: ")
    tanque = verificar_nombre(n)
    n = input("BRUJO: ")
    brujo = verificar_nombre(n)
    n = input("ARQUERO: ")
    arquero = verificar_nombre(n)
    
    print(f"Tus personajes son {tanque}, {brujo} y {arquero}")
    
    TANQUE_HP = 200
    BRUJO_HP = 150
    ARQUERO_HP = 100
    ENEMIGO_HP = 1000
    
    print("Se acerca un enemigo")
    
    while ENEMIGO_HP > 0:
        daño = turno_tanque(tanque)
        ENEMIGO_HP -= daño
        print(daño)
        print(f"ENEMIGO: {ENEMIGO_HP})")
        
if __name__=="__main__":
    main()