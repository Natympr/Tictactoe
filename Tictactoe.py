from random import randrange
from libreria import board

MACHINE = 'X'
HUMAN = 'O'

def lista_celdas_vacias(tablero):
    return [x for x in tablero if tablero[x] is None] 

def is_tablero_empty(tablero):
    return len(lista_celdas_vacias(tablero)) == 9

def is_tablero_lleno(tablero):
    return len(lista_celdas_vacias(tablero)) == 0
    

def movimiento_maquina(tablero):
    if is_tablero_empty(tablero):
        tablero[5] = MACHINE
    else:
        l = lista_celdas_vacias(tablero)
        tablero[l[randrange(len(l))]] = MACHINE

def movimiento_humano(tablero):
    while True:
        celda = int(input("Ingrese movimiento: "))
        if tablero[celda] is None:
            tablero[celda] = HUMAN
            break
        
        else:
             print("la celda esta ocupada o fuera del rango. Intenta de nuevo.")

#def es_ganador(tablero, jugador):
 #   return ((tablero[1] == tablero[2] == tablero[3] == jugador) or
  #          (tablero[4] == tablero[5] == tablero[6] == jugador) or
   #         (tablero[7] == tablero[8] == tablero[9] == jugador) or
    #        (tablero[1] == tablero[4] == tablero[7] == jugador) or
     #       (tablero[2] == tablero[5] == tablero[8] == jugador) or
      #      (tablero[3] == tablero[6] == tablero[9] == jugador) or
       #     (tablero[1] == tablero[5] == tablero[9] == jugador) or
        #    (tablero[3] == tablero[5] == tablero[7] == jugador))    



def es_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # filas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columnas
        [1, 5, 8], [3, 5, 7]              # diagonales
    ]
    for combo in combinaciones_ganadoras:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == jugador:
            return True
    return False

def main():
    tablero = {x: None for x in range(1, 10)}

    while True:
        movimiento_maquina(tablero)
        board(tablero)

        if es_ganador(tablero, MACHINE):
            print("Te gané :) ")
            break

        if is_tablero_lleno(tablero):
            print ("Empate")
            break

        movimiento_humano(tablero)
        board(tablero)

        if es_ganador(tablero, HUMAN):
            print("¡Ganaste!")
            break


if __name__ == '__main__':
    main()  