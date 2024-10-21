machine = 'X'
human = 'O'

tablero = {x: None for x in range(1,10)}


def celda(numero):
    return numero if tablero[numero] is None else tablero[numero]
def board():
    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|   ", celda(1), "  |   ", celda(2), "  |   ", celda(3), "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|   ", celda(4), "  |   ", celda(5), "  |   ", celda(6), "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")
    print("|        |        |        |")
    print("|   ", celda(7), "  |   ", celda(8), "  |   ", celda(9), "  |")
    print("|        |        |        |")
    print("+--------+--------+--------+")

    
board()