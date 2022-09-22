from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

ancho_pantalla, alto_pantalla = 1000,1000

# Rotación del eje.
# Rotar 30 grados alrededor de la linea (0.1,0.2,0)
rotacion_base = [30, -0.1, 0.1, 0]

vertices = (
    (-0.5, -0.5, 0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, 0.5, 0.5),
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



def inicializar():

    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(60, 600/600, 0.1, 50)
    #glTranslatef(0.0, 0.0, -2.0)
    gluLookAt(0,0,5,0,0,0,0,1,0)

    #glOrtho(-1,1,-1,1,-1,1)


    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Borrar la pantalla
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def ejes():
    #glPushMatrix()
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
    #glPopMatrix()

def square(r,g,b):
    glColor3f(r,g,b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glEnd()

def cubo(size):
    glPushMatrix()

    # Vamos generando el cubo en base a transformaciones de cuadrados
    # 1a cara = Frente
    glPushMatrix()
    glScalef(size,size,size)
    square(1,0.8,0.8)
    glPopMatrix()

    # 2a cara = Derecha
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(90,0,1,0)
    square(0.8,1,0.8)
    glPopMatrix()


    # 3a cara = Arriba
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(-90,1,0,0)
    square(0.8,0.8,1)
    glPopMatrix()

    # 3a cara = Atras
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(-180,1,0,0)
    square(0.3,1,0.3)
    glPopMatrix()

    glPopMatrix()
def display():
    inicializar()
    ejes()
    cubo(1)
    glFlush()

def main():
    glutInit(sys.argv)
    #glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    #https://stackoverflow.com/questions/59510466/pyopengl-depth-test-doesnt-do-anything
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH )
    glutInitWindowSize(ancho_pantalla, alto_pantalla)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(u'Matrix Operations')
    glutDisplayFunc(display)
    glutMainLoop()


main()
