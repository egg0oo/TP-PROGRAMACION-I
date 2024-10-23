from verificacion import nombrar
from verificacion import verificar

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
                "acciones":acciones,
                "daño total":[0,0,0]
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
                "vida":vida,
                "ataque":ataque,
                }
        linea = file.readline()
        file.close()
        return enemigos
        
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
    
    personajes = cargar_stats("stats.text")
    
    print(personajes)
    
    enemigos = cargar_stats_enemigos("stats_enemigos.text")
    
    print(enemigos)
    
if __name__ == "__main__":
    main()