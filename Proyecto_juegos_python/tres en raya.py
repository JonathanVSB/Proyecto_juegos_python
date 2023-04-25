
from xmlrpc.client import boolean
import PiedraPapelTijera

def comprobar(tablero):
    for x in tablero:
        if (tablero[0][0]== tablero[1][1]== tablero[2][2]) or (tablero[2][0]== tablero[1][1]== tablero[0][2]):
            return True 
        elif (tablero[0][0]== tablero==[0][1]==tablero[0][2]) or (tablero[1][0]==tablero==[1][1]==tablero[1][2]) or (tablero[2][0]==tablero==[2][1]==tablero[2][2]):
            return True
        
        elif (tablero[0][0]==tablero[1][0]==tablero[2][0]) or (tablero[0][1]==tablero[1][1]==tablero[2][1]) or (tablero[0][2]==tablero[1][2]==tablero[2][2]):
            return True
        else:
            return False
def mostrarTablero(tablero):
    for fila in tablero:
        print('-'*13)
        for j in fila:
            print('| ', j, ' ', end='', sep='')
        print('|')
    print('-'*13)
def jugada (tablero, posicion, jugador):
    posicion -=1
    estaOcupado = tablero[posicion // 3][posicion % 3] == 'X' or tablero[posicion // 3][posicion % 3] =='0'
    if estaOcupado:
        return False
    else:
        tablero[posicion // 3][posicion % 3] =jugador
        return True

def Tres_En_Raya():        
    jugador1= PiedraPapelTijera.Pedir_jugador()
    jugador2= PiedraPapelTijera.Pedir_jugador()


    base = []
    fila = []
    for i in range(1, 10):
        fila.append(i)
        if i % 3 == 0:
            base.append(fila)
            fila = []

    tablero = base[:]
    jugador =('X', '0')
    jugadores=(jugador1, jugador2)
    contador = 0
    mensaje = True

    while True:
        if mensaje:
            mostrarTablero(tablero)
            print('juega', jugadores[contador % 2], end='')
            posicion = int(input(' Ingrese posicion: '))
        else:
            print('posicion invalida', end = '')
            posicion = int(input(" Vuelva a ingresar posicion: "))
        
        
        mensaje = jugada(tablero, posicion, jugador[contador % 2])

        if comprobar(tablero)==True:
            mostrarTablero(tablero)
            print('Ganador', jugadores[contador % 2])
            break
                
        if contador == 8:
            print("Empate, nadie gana")
            break
        if mensaje:
            contador +=1



