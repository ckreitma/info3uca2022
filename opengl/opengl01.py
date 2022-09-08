# https://pharos.sh/breve-introduccion-a-opengl-en-python-con-pyopengl/
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500


def square():
    glColor3f(1.0, 0.8, 0.6)
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()


def triangulo1():
    glColor3f(0.5, 0.9, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 50)
    glVertex2f(300, 200)
    glVertex2f(250, 100)
    glVertex2f(50, 400)
    glVertex2f(80, 430)
    glVertex2f(70, 400)
    glEnd()


def cuadrilatero2():
    glColor3f(0.80, 0.5, 0.9)
    glBegin(GL_QUADS)
    glVertex2f(150, 250)
    glVertex2f(450, 300)
    glVertex2f(350, 350)
    glVertex2f(150, 300)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 2.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    square()
    cuadrilatero2()
    triangulo1()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Primitivas Cuadrilátero y Triángulos")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()