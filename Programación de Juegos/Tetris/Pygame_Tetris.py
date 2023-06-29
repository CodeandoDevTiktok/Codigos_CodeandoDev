import pygame
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
NARANJA = (255, 165, 0)

# Dimensiones de los bloques y el tablero de juego
ANCHO_BLOQUE = 30
ALTO_BLOQUE = 30
COLUMNAS = ANCHO // ANCHO_BLOQUE
FILAS = ALTO // ALTO_BLOQUE

# Matriz del tablero de juego
tablero = [[NEGRO for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Piezas de Tetris
piezas = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]

# Posición y forma actual de la pieza en juego
posicion_x = COLUMNAS // 2 - 2
posicion_y = 0
forma_actual = random.choice(piezas)
color_actual = random.choice([CYAN, MAGENTA, NARANJA, AMARILLO, ROJO, VERDE, AZUL])

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Tetris")

# Función para dibujar el tablero de juego
def dibujar_tablero():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(
                ventana,
                tablero[fila][columna],
                (
                    columna * ANCHO_BLOQUE,
                    fila * ALTO_BLOQUE,
                    ANCHO_BLOQUE,
                    ALTO_BLOQUE,
                )
            )

# Función para dibujar la pieza en juego
def dibujar_pieza():
    for fila in range(len(forma_actual)):
        for columna in range(len(forma_actual[0])):
            if forma_actual[fila][columna]:
                pygame.draw.rect(
                    ventana,
                    color_actual,
                    (
                        (posicion_x + columna) * ANCHO_BLOQUE,
                        (posicion_y + fila) * ALTO_BLOQUE,
                        ANCHO_BLOQUE,
                        ALTO_BLOQUE,
                    ),
                )

# Función para verificar si la posición de la pieza es válida
def verificar_posicion():
    for fila in range(len(forma_actual)):
        for columna in range(len(forma_actual[0])):
            if (
                forma_actual[fila][columna]
                and (
                    posicion_x + columna < 0
                    or posicion_x + columna >= COLUMNAS
                    or posicion_y + fila >= FILAS
                    or tablero[posicion_y + fila][posicion_x + columna] != NEGRO
                )
            ):
                return False
    return True

# Función para colocar la pieza en el tablero
def colocar_pieza():
    for fila in range(len(forma_actual)):
        for columna in range(len(forma_actual[0])):
            if forma_actual[fila][columna]:
                tablero[posicion_y + fila][posicion_x + columna] = color_actual

# Función para eliminar filas completas
def eliminar_filas_completas():
    filas_completas = []
    for fila in range(FILAS):
        if NEGRO not in tablero[fila]:
            filas_completas.append(fila)
    for fila_completa in filas_completas:
        del tablero[fila_completa]
        tablero.insert(0, [NEGRO for _ in range(COLUMNAS)])

# Ciclo principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicion_x -= 1
                if not verificar_posicion():
                    posicion_x += 1
            elif evento.key == pygame.K_RIGHT:
                posicion_x += 1
                if not verificar_posicion():
                    posicion_x -= 1
            elif evento.key == pygame.K_DOWN:
                posicion_y += 1
                if not verificar_posicion():
                    posicion_y -= 1
            elif evento.key == pygame.K_SPACE:
                while verificar_posicion():
                    posicion_y += 1
                posicion_y -= 1
                colocar_pieza()
                eliminar_filas_completas()
                forma_actual = random.choice(piezas)
                color_actual = random.choice(
                    [CYAN, MAGENTA, NARANJA, AMARILLO, ROJO, VERDE, AZUL]
                )

    if verificar_posicion():
        posicion_y += 1
    else:
        colocar_pieza()
        eliminar_filas_completas()
        forma_actual = random.choice(piezas)
        color_actual = random.choice([CYAN, MAGENTA, NARANJA, AMARILLO, ROJO, VERDE, AZUL])
        posicion_x = COLUMNAS // 2 - 2
        posicion_y = 0
        if not verificar_posicion():
            jugando = False

    # Limpiar la ventana
    ventana.fill(BLANCO)

    # Dibujar el tablero y la pieza en juego
    dibujar_tablero()
    dibujar_pieza()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(5)

# Salir del juego
pygame.quit()
