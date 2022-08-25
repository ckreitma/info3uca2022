# A Python3 program to check if a given point
# lies inside a given polygon
# Refer https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# This code is contributed by Vikas Chitturi
# for explanation of functions onSegment(),
# orientation() and doIntersect()

# Define Infinite (Using INT_MAX
# caused overflow problems)

import pygame
from math import sin, cos, pi
from time import sleep
from operator import itemgetter

INT_MAX = 10000

COLOR_FUERA = (200,10,10)
COLOR_DENTRO = (10,10,200)
COLOR_LINEA = (10,200,10)




# Given three colinear points p, q, r,
# the function checks if point q lies
# on line segment 'pr'


def onSegment(p: tuple, q: tuple, r: tuple) -> bool:

    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
        return True

    return False

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are colinear
# 1 --> Clockwise
# 2 --> Counterclockwise

# Explicación en https://www.geeksforgeeks.org/orientation-3-ordered-points/


def orientation(p: tuple, q: tuple, r: tuple) -> int:

    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))

    if val == 0:
        return 0  # Collinear
    if val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclock


def doIntersect(p1, q1, p2, q2):

    # Find the four orientations needed for
    # general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are colinear and
    # p2 lies on segment p1q1
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True

    # p1, q1 and q2 are colinear and
    # q2 lies on segment p1q1
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are colinear and
    # p1 lies on segment p2q2
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are colinear and
    # q1 lies on segment p2q2
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True

    return False

# Returns true if the point p lies
# inside the polygon[] with n vertices


def is_inside_polygon(points: list, p: tuple) -> bool:

    n = len(points)

    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False

    # Create a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
    count = i = 0

    while True:
        next = (i + 1) % n

        # Check if the line segment from 'p' to
        # 'extreme' intersects with the line
        # segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(points[i], points[next], p, extreme)):

            # If the point 'p' is colinear with line
            # segment 'i-next', then check if it lies
            # on segment. If it lies, return true, otherwise false
            if orientation(points[i], p, points[next]) == 0:
                return onSegment(points[i], p, points[next])
            count += 1
        i = next
        if (i == 0):
            break

    # Return true if count is odd, false otherwise
    return (count % 2 == 1)

def is_inside_polygon2(points: list, p: tuple) -> bool:
    cn = 0    # the crossing number counter

    # repeat the first vertex at end
    points = tuple(points[:])+(points[0],)

    # loop through all edges of the polygon
    for i in range(len(points)-1):   # edge from V[i] to V[i+1]
        if ((points[i][1] <= p[1] and points[i+1][1] > p[1])   # an upward crossing
                or (points[i][1] > p[1] and points[i+1][1] <= p[1])):  # a downward crossing
            # compute the actual edge-ray intersect x-coordinate
            # Como son rectas, se toman las proporciones de x e y (pendiente) y se verifica que esté en el rango
            vt = (p[1] - points[i][1]) / float(points[i+1][1] - points[i][1])
            if p[0] < points[i][0] + vt * (points[i+1][0] - points[i][0]):  # P[0] < intersect
                cn += 1  # a valid crossing of y=P[1] right of P[0]

    return cn % 2   # 0 if even (out), and 1 if odd (in)

def leer_puntos(archivo='./pygame/dino.txt'):
    # Toma el archivo y crea una lista de puntos.
    puntos = []
    datos = open(archivo)
    try:
        for linea in datos:
            x, y = linea.split(',')
            puntos.append((int(x), int(y)))
    except:
        print(f'Error al abrir el archivo {archivo}')
    finally:
        datos.close()
    return puntos

def poligono(canvas, lista_puntos, color):
    puntos = lista_puntos
    p1 = puntos[0]
    linea = 0
    for p2 in puntos[1:]:
        #print(f'Linea={linea} p1={p1} p2={p2}')
        pygame.draw.aaline(canvas, color, p1, p2)
        p1 = p2
        linea+=1

def pintar_linea(canvas,fila,puntos,color_fuera,color_dentro):
    min_x = res = min(puntos, key=itemgetter(0))[0]
    max_x = res = max(puntos, key=itemgetter(0))[0]


    for x in range(min_x-10,max_x+10):
        if is_inside_polygon2(puntos,(x,fila)):
            pygame.draw.line(canvas,color_dentro,(x,fila),(x,fila))
        else:
            pygame.draw.line(canvas,color_fuera,(x,fila),(x,fila))

    pygame.display.update()
def pintar_poligono(canvas,puntos,color_fuera,color_dentro):
    min_y = res = min(puntos, key=itemgetter(1))[1]
    max_y = res = max(puntos, key=itemgetter(1))[1]
    for y in range(min_y-10,max_y+10):
        pintar_linea(canvas,y,puntos,color_fuera,color_dentro)
# Driver code
if __name__ == '__main__':
    pygame.init()

    color = (20, 20, 20)
    rect_color = (600, 600, 0)

    dino = leer_puntos(archivo='./pygame/dino.txt')

    # CREATING CANVAS
    canvas = pygame.display.set_mode((600, 600))

    # TITLE OF CANVAS
    pygame.display.set_caption("Polígono a Partir de Archivo")

    exit = False

    while not exit:
        canvas.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        poligono(canvas, dino, COLOR_LINEA)
        pintar_poligono(canvas,dino, COLOR_FUERA, COLOR_DENTRO)
        pygame.display.update()