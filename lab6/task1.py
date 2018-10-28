import numpy as np
import math

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

file = open('tocke.txt', 'r')

points = []
for line in file:
    coordinates = line.split(' ')
    x = int(coordinates[0])
    y = int(coordinates[1])
    points.append((x, y))

n = len(points) - 1
nfac = math.factorial(n)
def getPointForT(t):
    newPoint = (0, 0)
    for i in range(0, n + 1):
        point = points[i]
        coeficient = (1.0 * math.factorial(i) * math.factorial(n-i))
        b = nfac * (t**i) * ((1 - t)**(n - i)) / coeficient
        newPoint = (newPoint[0] + point[0] * b, newPoint[1] + point[1] * b)
    return newPoint

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

    glBegin(GL_LINE_STRIP)
    for t in range(0, 101):
        point = getPointForT(t/100.0)
        glVertex2f(point[0], point[1])
    glEnd()

    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(100, 100)
glutCreateWindow('Dots_are_line')
glClearColor(0.0,0.0,0.0,0.0)
glClear(GL_COLOR_BUFFER_BIT)

glViewport(0, 0, 1000, 1000)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-1.0, 5.0, -1.0, 5.0)
glutDisplayFunc(display)
glutMainLoop()
