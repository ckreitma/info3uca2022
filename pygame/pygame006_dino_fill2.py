import pygame
import time
import numpy as np
ancho = 1200
alto = 900

BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
ROJO = (255, 10, 10)

# Ecuación de la recta.
# y = mx + b  m=pendiente, b=intersección con eje y.


def slope_intercept(x0, y0, x1, y1):
    if x1 != x0:
        a = (y1 - y0) / (x1 - x0)
        b = y0 - a * x0
        return a, b
    return 0, 0


def valor_y(punto0, punto1, x):
    """
    Esta función calculará el valor de la y correspondiente a
    la ecuación de la recta.
    y = mx + b
    m = pendiente
    b = intersección con el eje vertical
    """
    x0, y0 = punto0
    x1, y1 = punto1

    m, b = slope_intercept(x0, y0, x1, y1)

    # Faltan controlar casos extremos. Pendiente infinita.
    return m*x + b


def rellenar(screen, puntos, color_fuera=ROJO, color_dentro=BLANCO):
    p = np.array(puntos)
    miny, maxy = p[:, 1].min(), p[:, 1].max()
    for pos_y in range(miny, maxy):
        escanear_linea(screen, puntos, pos_y=pos_y, color_dentro=color_dentro, color_fuera=color_fuera)


def encontrar_lado(punto0, punto1, punto):
    """ Calcula el lado en el cual se encuentra
    un punto respecto a una recta (segmento)

    Args:
        punto0 (punto): par inicial
        punto1 (punto):  par final
        punto (punto): Punto

    Returns:
        int:
            -1 Si está a la izquierda
            +1 Si está a la derecha
            -2 Fuera de rango
            0  Si no se intersecan
    """
    x0, y0 = punto0
    x1, y1 = punto1
    x, y = punto
    x_max = max(x0, x1)
    x_min = min(x0, x1)
    y_max = max(y0, y1)
    y_min = min(y0, y1)

    if x < x_min or x > x_max or y < y_min or y > y_max:
        return -2

    y_punto = int(valor_y(punto0, punto1, x))
    # print(f'<{x},{y_punto}>')
    if y < y_punto:
        return 1
    if y > y_punto:
        return -1
    return 0


def escanear_linea(screen, puntos, pos_y, color_fuera=ROJO, color_dentro=BLANCO):
    """Dibuja una línea en el screen a la altura "pos_y"
    Args:
        screen ([type]): [description]
        puntos (lista de puntos): lista de puntos
    """
    # Primero vamos a encontrar el menor y el mayor de las x e y para no barrer toda la pantalla.
    p = np.array(puntos)
    minx, maxx, miny, maxy = p[:, 0].min(), p[:, 0].max(), p[:, 1].min(), p[:, 1].max()
    #print(f'Los puntos extremos son: {minx} {maxx} {miny} {maxy}')

    # En el caso de que la altura no esté en el rango retornamos
    if pos_y < miny or pos_y > maxy:
        return

    # Nos posicionamos a la altura indicada y hacemos un ciclo para las x
    color = color_fuera
    interior = 0
    lados_anteriores = [-1]*(len(puntos)-1)  # Al comienzo nos encontramos a la "izquierda de todo"
    # Nos movemos horizontalmente
    for x in range(minx-10, maxx+1):
        lados_actuales = [0]*(len(puntos)-1)
        for i in range(0, len(puntos)-1):
            # Vemos en qué lado de esa linea "i" nos encontramos.
            lados_actuales[i] = encontrar_lado(puntos[i], puntos[i+1], (x, pos_y))
        total_de_ceros = 0
        for i in range(0, len(puntos)-1):
            if lados_actuales[i] == 0 or (lados_actuales[i] == -1 and lados_anteriores[i] == 1) or (lados_actuales[i] == 1 and lados_anteriores[i] == -1):
                total_de_ceros += 1
        if total_de_ceros >= 1:
            interior = 1 - interior

        print(f'Total de ceros = {total_de_ceros}')
        #print(f'Lados anteriores para x={x}: {lados_anteriores} lados actuales={lados_actuales} Total cruces = {cantidad_cruces}')
        if interior == 0:  # La cantidad de cruces son pares
            #print(f'Cruce pares para x={x} pos_y={pos_y} anteriores:{lados_anteriores} lados actuales={lados_actuales}')
            color = color_fuera
        else:
            #print(f'Cruce impares para x={x} pos_y={pos_y} anteriores:{lados_anteriores} lados actuales={lados_actuales}')
            color = color_dentro
        lados_anteriores = lados_actuales
        pygame.draw.aaline(screen, color, (x, pos_y), (x, pos_y))


def leer_puntos(archivo='./pygame/dino.txt'):
    # Toma el archivo y crea una lista de puntos.
    puntos = []
    datos = open(archivo)
    try:
        for linea in datos:
            x, y = linea.split(',')
            #print(f'linea={linea} {x} {y}')
            puntos.append((int(x), int(y)))
    except:
        print(f'Error al abrir el archivo {archivo}')
    finally:
        datos.close()
    return puntos

# Dibuja los bordes partiendo de una lista de puntos.


def dibujar_bordes(screen, puntos, color=AZUL):
    for i in range(0, len(puntos)-1):
        pygame.draw.aaline(screen, color, puntos[i], puntos[i+1])


def principal():
    screen = pygame.display.set_mode((ancho, alto))
    running = True

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        archivo = './pygame/dino.txt'
        dibujar_bordes(screen, leer_puntos(archivo))
        #escanear_linea(screen, leer_puntos(archivo), 104)
        #escanear_linea(screen, leer_puntos(archivo), 354)
        #escanear_linea(screen, leer_puntos(archivo), 355)
        #escanear_linea(screen, leer_puntos(archivo), 356)
        rellenar(screen, leer_puntos(archivo))
        pygame.display.flip()
        # time.sleep(3)


if __name__ == '__main__':

    # Simulamos un escaneo
    #punto0 = (2, 1)
    #punto1 = (-1, -5)
    #y = -2
    # for x in range(-4, 6):
    #    print(f'Recta en {x}={valor_y(punto0,punto1,x)}')
    #    punto = (int(x), int(y))
    #    print(f'Lado: {punto0},{punto1},{punto} Lado={encontrar_lado(punto0,punto1,punto)}')

    #escanear_linea('hola', leer_puntos(), pos_y=200)
    principal()