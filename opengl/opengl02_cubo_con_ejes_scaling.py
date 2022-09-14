from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math


altura,ancho = 800,800
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def inicializar():
    # Borrar la pantalla
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(45, altura/ancho, 0.1, 50.0)

    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Inicializar la matriz.
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)

    # Ángulo,
    glRotatef(10, 0.2, 0.2, 0)

def ejes():
    # Eje x
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)

    glColor3f(0, 1, 0)
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)

    glColor3f(0, 0, 1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)

    glEnd()

def cubo():
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def cubo_scaled():
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0)

    matriz_escalado = [
        [0.3,0,0,0],
        [0,0.5,0,0],
        [0,0,0.5,0],
        [0,0,0,1],
    ]
    nuevos_vertices = scaling(vertices,matriz_escalado)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(nuevos_vertices[vertex][:3])
    glEnd()

def actualizar():
    inicializar()
    ejes()
    cubo()
    cubo_scaled()
    glFlush()

def scaling(lista_puntos,matriz):
    homogenea = []
    for p in lista_puntos:
        homogenea.append((p[0],p[1],p[2],1))

    transformada = np.matmul(homogenea,matriz)
    return transformada

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(altura, ancho)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cubo 3D sencillo con líneas")
    glutDisplayFunc(actualizar)
    glutMainLoop()


main()