from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

ancho_pantalla, alto_pantalla = 1000,1000

# Rotación del eje.
# Rotar 30 grados alrededor de la linea (0.1,0.2,0)
rotacion_base = [-15, -0.1, -0.1, 0]

vertices = (
    (0.4, -0.3, -0.2),
    (-0.5, -0.3, -0.2),
    (-0.5, -0.3, 0.35),
    (0.35, -0.3, 0.35),
    (-0.1, 0.65, 0.1),
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
)

colores = (
    (0.2,0.2,0.2),
    (0.2,0.4,0.5),
    (0.6,0.2,0.6),
    (0.3,0.7,0.2),
    (0.8,0.1,0.3),
    (0.4,0.2,0.7),
    (0.8,0.6,0.9),
    (0.2,0.9,0.6),
)


def transformar(lista_puntos,matriz):
    homogenea = []
    for p in lista_puntos:
        homogenea.append((p[0],p[1],p[2],1))

    transformada = np.matmul(homogenea,matriz)
    return transformada

def inicializar():
    # Borrar la pantalla
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(45, 600/600, 0.1, 50.0)

    # Matriz de proyección ortogonal
    #glOrtho(-1, 1, -1, 1, -1, 1)


    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

def ejes():
    # Borrar la pantalla
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glRotatef(rotacion_base[0], rotacion_base[1], rotacion_base[2], rotacion_base[3])

    # Le decimos a OPENGL que interprete los vértices como líneas
    glBegin(GL_LINES)

    # Dibuja el eje x en rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    # Dibuja el eje y en verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    # Dibuja el eje z en azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    glEnd()
    glPopMatrix()

def piramide():

    glPushMatrix()

    # Inicializar la matriz.
    glLoadIdentity()

    glRotatef(rotacion_base[0], rotacion_base[1], rotacion_base[2], rotacion_base[3])
    glTranslatef(0.0, 0.0, 0.0)

    # Ángulo,
    #glRotatef(45, 1, 0.3, 0.1)
    glBegin(GL_LINES)
    color = 0
    for edge in edges:
        glColor3f(colores[color][0], colores[color][1], colores[color][2])
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        color += 1
    glEnd()
    glPopMatrix()


def piramide2():
    glPushMatrix()

    # Inicializar la matriz.
    glLoadIdentity()

    glRotatef(rotacion_base[0], rotacion_base[1], rotacion_base[2], rotacion_base[3])
    glTranslatef(0.0, 0.0, 0.0)

    # Escalado.
    escalar = [[0.3,0,0,0],
               [0, 0.3, 0,0],
               [0, 0, 0.3,0],
               [0,0,0,1]
               ]


    # Escalado.
    rotar_z = [[math.cos(0.3),math.sin(0.3),0,0],
               [-math.sin(0.3), math.cos(0.3), 0,0],
               [0, 0, 1,0],
               [0,0,0,1]
               ]

    vertices_escalados=transformar(vertices,np.matmul(escalar,rotar_z))[:,:-1]

    glBegin(GL_LINES)
    color = 0
    for edge in edges:
        glColor3f(colores[color][0], colores[color][1], colores[color][2])
        for vertex in edge:
            glVertex3fv(vertices_escalados[vertex])
        color += 1
    glEnd()
    glPopMatrix()

def transformar1():
    ejes()
    piramide()
    piramide2()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(ancho_pantalla, alto_pantalla)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(u'Piramide con scaling')
    glutDisplayFunc(transformar1)
    glutMainLoop()


main()
