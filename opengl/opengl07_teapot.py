# https://codeloop.org/python-opengl-programming-drawing-teapot/
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)  # Apunta a la matriz de proyección
    glLoadIdentity()
    # Matriz de proyección ortogonal
    #glOrtho(-1, 1, -1, 1, -1, 0)

    # Ángulo, ratio, near, far
    gluPerspective(60, 600/600, 0, 10)
    gluLookAt(0,0,3,0,0,0,0,1,0)
    glMatrixMode(GL_MODELVIEW)
    glutSolidTeapot(0.6)
    #glutTeapot(0.6)
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Tetera")
glutDisplayFunc(draw)
glutMainLoop()
