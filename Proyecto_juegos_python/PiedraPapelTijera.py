from gettext import NullTranslations
from re import A


def Pedir_jugador():
    # Función para pedir el nomre del jugador
    jugador=str(input("Introduce el nombre del jugador:"))
    return jugador

def Numero_jugadores():
    # Con esta función registramos el número de jugadores del juego
    print("Introduce el número de jugadores: ")
    num=int(input("1-Jugador    2-Jugadores:  "))
    return num

def Menu_tirada(jugador):
    # ƒunción para registrar la tirada que hará el jugador en el piedra, papel y tijeras
    print("Cual es tu tirada jugador " +jugador)
    print("1-Piedra   2-Papel   3-Tijeras")
    tirada = int(input())

    return tirada

def Resolución(tirada1, tirada2):
    # Función que compara la mano de cada jugador para ver cual es el ganador de la ronda
    if tirada1 == tirada2:
        print("Ha sido un empate!")
        return 0

    elif tirada1 == 1 and tirada2== 3:
        print("Ha ganado el jugador 1")
        return 1

    elif tirada1 == 1 and tirada2 ==2:
        print("Ha ganado el jugador 2")
        return 2

    elif tirada1 == 2 and tirada2== 1:
        print("Ha ganado el jugador 1")
        return 1

    elif tirada1 == 2 and tirada2 ==3:
        print("Ha ganado el jugador 2")
        return 2

    elif tirada1 == 3 and tirada2 ==1:
        print("Ha ganado el jugador 2")
        return 2

    else:
        print("Ha ganado el jugador 1")
        return 1
        
def Aleatorio(a,b):
    # Función para generar números aleatorios 
    import random
    tirada= random.randint(a, b)

    return tirada

#=============================================================
#=============================================================


  


