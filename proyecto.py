
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
    return False

def tablero_lleno(tablero):
    return all(celda in ['X', 'O'] for fila in tablero for celda in fila)

def juego():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        fila = int(input("Ingresa la fila (0, 1, 2): "))
        columna = int(input("Ingresa la columna (0, 1, 2): "))

        if tablero[fila][columna] != " ":
            print("Esa casilla ya está ocupada. Intenta de nuevo.")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

juego()
