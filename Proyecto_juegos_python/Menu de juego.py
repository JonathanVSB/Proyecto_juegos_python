from importlib import import_module

import PiedraPapelTijera

# Código para hacer el menú de juego.
# El código constará de 4 opciones para elegir. 
# si el usuario introduce un valor inválido. seguirá pidiendo número

def Menu_Juego():
    # Función con el menú de selección de juego
    print("Menú APP Juegos:")
    print("1. Piedra, papel o tijera")
    print("2. El ahorcado")
    print("3. Tres en Raya:")
    print("4. Salir")

def Ahorcado():
    # Función con el código del juego del ahorcado
    import random
    import os

    palabras = ["CARAMELO", "CAFETERIA", "MARIPOSA", "CARRETERA", "TERMOMETRO",
                "ESCALERA", "CRUCIGRAMA", "MICROONDA", "PARTITURA", "ELEFANTE",
                "CARNICERO", "PEGAMENTO", "CIRUJANO", "MERMELADA", "ETIQUETA",
                "HERRAMIENTA", "ARMARIO", "HOGUERA", "ASCENSOR", "BELLOTA"]

    palabra = list(random.choice(palabras))

    print("esta es la solusion " +  str(palabra))

    horca = ["          !===========N",
            "                      N",
            "                      N",
            "                      N",
            "                      N",
            "                      N",
            "                      N",
            "    __________________N"]

    ahorcado = ["          !===========N",
                "          o           N",
                "        / | \         N",
                "        \ | /         N",
                "         / \          N",
                "        /   \         N",
                "       _\   /_        N",
                "    __________________N"]

    TodasLasLetras = []  # todas las letras dichas
    fallos = 1  # Contador de fallos
    resultado = []  # Lista con guiones a sustituir por letaras acertadas
    for i in range(len(palabra)):
        resultado.append("_")

    # Bucle principal del juego

    while True:
        os.system(" ;) ")

        print(" JUEGO DEL AHORCADO")
        print("********************************************")

        for i in range(fallos):
            print(ahorcado[i])
        for i in range(len(horca)-fallos):
            print(horca[i+fallos])

        print(";D")

        # Mostramos el resultado que se va a obteniendo

        print("     ", end="   ")
        for i in resultado:
            print(i, end="  ")

        print()
        print()

        # comprobamos si se ha acertado la palabras o se termino los intestos

        if resultado == palabra:
            print("HAS GANADO")
            break
        if fallos > 6:
            print("")
            print("La palabra era :"+str(palabra))
            print("HAS PERDIDO")
            break

        # BUCLE PARA QUE EL USUARIO ELIJA UNA LETRA

        while True:
            letra_usuario_sin_formato = input("Dime una letra: ") # aqui es donde el usuario introduce una letra 
            letra_usuario = letra_usuario_sin_formato.upper() # aqui cogemos la letra y la ponemos en mayuscula 
            if len(letra_usuario) != 1:
                print("Introduce una letra")
            elif letra_usuario in TodasLasLetras: # si el usuario dice una letra que ya halla dicho antes se le muestra este mensage 
                print("Esa letra ya la has dicho.")
            elif letra_usuario not in "QWERTYUIOPASDFGHJKLÑZXCVBNM": # aqui es para que solo me ponga una letra del abecedario español para que no ponga nincun otro mas caracter
                print("Introduce una letra ")
            else:
                TodasLasLetras.append(letra_usuario)
                break

        # comprobamos si la letras esta en la palabra, si esta sustituimos en el guion
        for i in range(len(palabra)):
            if palabra[i] == letra_usuario:
                resultado[i] = letra_usuario
        if letra_usuario not in palabra:
            fallos += 1

        print()
        print()  

def Rejugar():
    print("quieres volver a Jugar?")
    print("1- Sí   2- No")
    respuesta= int(input())

    return respuesta

def comprobar(tablero):
    # Comprueba las casillas del tablero para ver si se cumple la condición de Tres en raya
    for x in tablero:
         # 3 en raya Diagonal
        if (tablero[0][0]== tablero[1][1]== tablero[2][2]) or (tablero[2][0]== tablero[1][1]== tablero[0][2]):
            return True 
        # 3 en raya horizontal
        elif (tablero[0][0]== tablero[0][1]==tablero[0][2]) or (tablero[1][0]==tablero[1][1]==tablero[1][2]) or (tablero[2][0]==tablero[2][1]==tablero[2][2]):
            return True
        
        # 3 en raya vertical
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
    # Función con el juego del Tres en raya     
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
     
#=========================================================================================================
# Aquí empieza la opción 1. El juego del Piedra, Papel y Tijeras
#=========================================================================================================
Menu_Juego()
opcion = int(input("Elige un juego: "))

while opcion!=4:
    if opcion<1 or opcion>4:
        print("==========================")
        print("número de opcion Invalida")
        print("==========================")
    elif opcion== 1:
        cont=0
        con_Partidas=0
        print("========================")
        print("Has seleccionado: Piedra, papel o tijera")
        print("==========================")

        print("Bienvenido a Piedra - Papel - Tijera!!")
        print("Estas son las reglas:")
        print("1. Este Juego está hecho para 2 jugadores")
        print("2. ganará quien consiga antes 3 Victorias")
        print("3. Si el juego va a alargarse en la sexta ronda declararé a un ganador")
        print("Puedes elegir jugar contra otro jugador, o contra la máquina: ")
        respuesta = int()

        while respuesta!=2:
            jugadores=PiedraPapelTijera.Numero_jugadores()

            # Código para Partida de 1 Jugador.(Jugador vs. Máquina)
            if jugadores==1:
                
                    cont2=0
                    jugador1=PiedraPapelTijera.Pedir_jugador() # El jugador introduce su nombre
                    print("Bienvenido jugador " +jugador1)
                    print("Vamos a dar inicio al juego")
                    while cont<3 and cont2<3 and con_Partidas<6:
                        tirada1=PiedraPapelTijera.Menu_tirada(jugador1) # Función que registra la mano que sacará el jugador según el número que introduzca
                        tirada2=PiedraPapelTijera.Aleatorio(1,3)# La tirada de la máquina la genera una función de aleatorios
                        
                        resultado=int(PiedraPapelTijera.Resolución(tirada1,tirada2))# Función que se encarga de resolver el ganador de cada ronda
                        
                        #Esta parte del código registra los puntos que tiene cada jugador, así como el número de rondas que se han jugado
                        if resultado==1:
                            cont+=1
                            con_Partidas+=1
                        
                        elif resultado==2 :
                            cont2+=1
                            con_Partidas+=1

                        else:
                            con_Partidas+=1

                    if cont>cont2:
                        print("====================================")
                        print ("El ganador es el jugador " +jugador1)
                        print("====================================")

                    elif cont2>cont:
                        print("====================================")
                        print ("Ha ganado la máquina")
                        print("====================================")

                    else:
                        print("====================================")
                        print("Ha sido empate!! Ningun Jugador gana")
                        print("====================================")

                    
            # Código para Partida de 2 Jugadores.(Jugador1 vs. Jugador2)
            elif jugadores==2:
                
                    cont2=0 
                    jugador1=PiedraPapelTijera.Pedir_jugador() # El jugador 1 introduce su nombre
                    jugador2=PiedraPapelTijera.Pedir_jugador() # El jugador 2 introduce su nombre
                    print("Bienvenidos jugadores " +jugador1+ " y " +jugador2)
                    print("Vamos a dar inicio al juego")
                    while cont<3 and cont2<3 and con_Partidas<6: # será detenido cuando un jugador gane 3 rondas, o cuando se hayan jugado 6

                        tirada1=PiedraPapelTijera.Menu_tirada(jugador1) # Función que registra la mano que sacará el jugador 1 según el número que introduzca
                        tirada2=PiedraPapelTijera.Menu_tirada(jugador2) # Función que registra la mano que sacará el jugador 2 según el número que introduzca
                        resultado=int(PiedraPapelTijera.Resolución(tirada1,tirada2)) # Función que se encarga de resolver el ganador de cada ronda comparando las tiradas de cada uno

                        #Esta parte del código registra los puntos que tiene cada jugador, así como el número de rondas que se han jugado
                        if resultado==1:
                            cont+=1
                            con_Partidas+=1
                        
                        elif resultado==2 :
                            cont2+=1
                            con_Partidas+=1

                        else:
                            con_Partidas+=1

                    if cont>cont2:
                        print("====================================")
                        print ("El ganador es el jugador " +jugador1)
                        print("====================================")

                    elif cont2>cont:
                        print("====================================")
                        print ("El ganador es el jugador " +jugador2)
                        print("====================================")

                    else:
                        print("====================================")
                        print("Ha sido empate!!")
                        print("====================================")

            respuesta=Rejugar() # Se le pedirá al/los jugador/res, si quieren volver a Jugar 

#==============================================================================
# Aquí empieza la opción 2. El juego del Ahorcado
#==============================================================================
    elif opcion== 2:
        print("========================")
        print("Has seleccionado: El ahorcado")
        print("==========================")

        Ahorcado() # Función que contiene el juego del ahorcado
        respuesta = Rejugar()

        while respuesta!=2:
            Ahorcado() 
            respuesta= Rejugar() # Se le pedirá al/los jugador/res, si quieren volver a Jugar 

#==============================================================================
# Aquí empieza la opción 3. El juego del Tres en Raya
#==============================================================================
  

    elif opcion== 3:
        print("========================")
        print("Has seleccionado: Tres en Raya")
        print("==========================")



        Tres_En_Raya() # Se llama a la función que contiene el juego del tres en raya
        respuesta = Rejugar() # Se le pedirá al/los jugador/res, si quieren volver a Jugar 

        while respuesta !=2:
            Tres_En_Raya() 
            respuesta = Rejugar() # Se le pedirá al/los jugador/res, si quieren volver a Jugar 

    
    Menu_Juego()
    opcion = int(input("Elige un juego: "))

