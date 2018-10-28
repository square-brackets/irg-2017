import numpy as np
import math

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

eps = 100
m = 16
umin = -1.0
umax = 1.0
vmin = -1.2
vmax = 1.2
c = (0.32, 0.043)

xmax = 1000
ymax = 1000

def square(number):
    a = number[0]
    b = number[1]
    return (a**2 - b**2, 2 * a * b)

def add(numberA, numberB):
    return (numberA[0] + numberB[0], numberA[1] + numberB[1])

def absolute(number):
    return math.sqrt(number[0] ** 2 + number[1] ** 2)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for x0 in range(0, xmax):
        for y0 in range(0, ymax):
            u0 = (umax - umin) / xmax * x0 + umin
            v0 = (vmax - vmin) / ymax * y0 + vmin

            k = -1
            z = (u0, v0)

            r = 0

            while r < eps and k < m:
                k += 1
                z = add(square(z), c)
                r = absolute(z)

            glBegin(GL_POINTS)
            color = float(k) / float(m)
            glColor3f(color, color, color)
            glVertex2f(x0, y0)
            print (x0, y0, color)
            glEnd()

    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(100, 100)
glutCreateWindow('Dots_are_line')
glClearColor(0.0, 0.0, 0.0, 0.0)
glClear(GL_COLOR_BUFFER_BIT)

glViewport(0, 0, 1000, 1000)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0.0, 1000.0, 0.0, 1000.0) #kocka i teapot
glutDisplayFunc(display)
glutMainLoop()
