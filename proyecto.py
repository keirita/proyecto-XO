print("Hola a todos")
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)



def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
 