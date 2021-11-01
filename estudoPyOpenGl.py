import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)



def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)        # GL_POINTS -> GL_LINES
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 1.0)         # Added another Vertex specifying end coordinates of line
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Point")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()