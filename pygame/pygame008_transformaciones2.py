# Ejemplo de Polígono simple a partir de lista de puntos de archivo
import pygame
import numpy as np
import math



def poligono(canvas, lista_puntos, color):
    puntos = lista_puntos
    p1 = puntos[0]
    linea = 0
    for p2 in puntos[1:]:
        print(f'Linea={linea} p1={p1} p2={p2}')
        #pygame.draw.aaline(canvas, color, (p1[0],p1[1]),(p2[0],p2[1]))
        pygame.draw.line(canvas, color, (p1[0],p1[1]),(p2[0],p2[1]),5)
        p1 = p2
        linea+=1


def escalar(lista_puntos,factor_x,factor_y):
    modificada = []
    for p in lista_puntos:
        x = p[0]*factor_x
        y = p[1]*factor_y
        modificada.append((x,y))
    return modificada

def rotar(lista_puntos,angulo):
    modificada = []
    for p in lista_puntos:
        x = p[0]*math.cos(angulo) - p[1]*math.sin(angulo)
        y = p[0]*math.sin(angulo) + p[1]*math.cos(angulo)
        modificada.append((x,y))
    return modificada

def rotar_punto(lista_puntos,angulo,punto):
    return trasladar(rotar(trasladar(lista_puntos,-punto[0],-punto[1]),angulo),punto[0],punto[1])

def escalar_punto(lista_puntos,factor_x,factor_y,punto):
    return trasladar(escalar(trasladar(lista_puntos,-punto[0],-punto[1]),factor_x,factor_y),punto[0],punto[1])

def trasladar(lista_puntos,delta_x,delta_y):
    modificada = []
    for p in lista_puntos:
        x = p[0]+delta_x
        y = p[1]+delta_y
        modificada.append((x,y))
    return modificada


# Driver code
if __name__ == '__main__':
    pygame.init()

    color = (20, 20, 20)
    rect_color = (255, 100, 0)

    # CREATING CANVAS
    canvas = pygame.display.set_mode((600, 600))

    # TITLE OF CANVAS
    pygame.display.set_caption("UCA Transformaciones")

    exit = False
    lista_puntos = ((60,40),(250,250),(100,300),(150,200),(60,40))

    puntos_escalados = escalar(lista_puntos,1.3,1.5)
    puntos_escalados_chico = escalar(lista_puntos,0.2,0.3)
    rotado1 = rotar(lista_puntos,0.45)
    rotado2 = rotar(lista_puntos,-0.6)
    trasladado1 = trasladar(lista_puntos,40,100)
    rotado_punto = rotar_punto(lista_puntos, math.pi, (120,200))
    escalado_punto = escalar_punto(lista_puntos,2,2,(180,200))

    while not exit:
        canvas.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        poligono(canvas, lista_puntos, rect_color)
        #poligono(canvas, puntos_escalados, (50,100,24))
        #poligono(canvas, puntos_escalados_chico, (150,0,200))
        #poligono(canvas, rotado1, (150,0,200))
        #poligono(canvas, rotado2, (10,200,200))
        #poligono(canvas, trasladado1, (10,200,200))
        poligono(canvas, rotado_punto, (10,200,200))
        #poligono(canvas, escalado_punto, (10,200,200))
        pygame.display.update()