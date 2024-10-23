from verificacion import nombrar
from verificacion import verificar

def cargar_stats(archivo, nombres):
    try:
        personajes = {}
        file = open(archivo, "r")
    except IOError:
        print("No se pudo abrir el archivo")
    else:
        for linea in file:
            datos = linea.strip().split(";")
            rol = datos[0]
            vida = int(datos[1])
            acciones = datos[2:]

            # Para reemplazar por su nombre asignado.
            personajes[nombres[rol]] = {
                 "vida": vida,
                 "acciones": acciones,
                 "daño total": [0, 0, 0]
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
            ataque = int(datos[2])
            enemigos[enemigo] = {
                "vida": vida,
                "ataque": ataque,
            }
        file.close()
        return enemigos

def main():
    cad = "EL LEGADO PERDIDO".center(29, "=")
    print(cad)
    
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

    personajes = cargar_stats("stats.text", nombres)
    print(personajes)
    
    enemigos = cargar_stats_enemigos("stats_enemigos.text")
    print(enemigos)

if __name__ == "__main__":
    main()