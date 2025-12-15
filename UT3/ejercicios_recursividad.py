# FACTORIAL RECURSIVO
def factorial(n):
    if n == 0:
        return 1
    else:
        return(factorial(n-1) * n)
    
print(factorial(4))

numero = int(input("introduce un numero para acer la torre de Hanoi: "))

torres = {
    "A": list(range(numero, 0, -1)),
    "B": [],
    "C": []
}


# TORRES DE HANOI RECURSIVO
def mover(origen, destino, torres):
    movido = torres[origen].pop()
    torres[destino].append(movido)
    print(f"Movido disco {movido} de {origen} a {destino}\n")

def imprimir_estado(torres):
    print("Estado de las torres:")
    print("Torre A:", torres["A"])
    print("Torre B:", torres["B"])
    print("Torre C:", torres["C"])
    print("----------------")

def hanoi(n, origen, apoyo, destino):
    if n == 1: 
        mover(origen, destino, torres)
        imprimir_estado(torres)
        return
    else:
        hanoi(n-1, origen, destino, apoyo)
        mover(origen, destino, torres)
        imprimir_estado(torres)
        hanoi(n-1, apoyo, origen, destino) 

imprimir_estado(torres)
hanoi(numero, "A", "B", "C")


# CABALLO DE AJEDREZ RECURSIVO
    
MOVIMIENTOS_CABALLO = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

TABLERO = [8][8]
for i in range(8):
    for j in range(8):
        TABLERO[i][j] = -1

def es_movimiento_valido(x, y, tablero):
    return 0 <= x < 8 and 0 <= y < 8 and tablero[x][y] == -1

def mover():
    print("")

def resolver_recorrido_caballo(n):
    for (mx, my) in MOVIMIENTOS_CABALLO:
        movimiento_x = 0
        movimiento_y = 0
        if es_movimiento_valido(movimiento_x, movimiento_y, TABLERO):
            
            break