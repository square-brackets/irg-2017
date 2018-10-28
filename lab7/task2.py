import numpy as np
import math

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

ka = 0.5
kd = 0.5

sourceIntensity = 1
destinationIntensity = 0.7

def transform(point, T, P):
    return np.matrix([point[0], point[1], point[2], 1]) * T * P

def serializeLine(line):
    coordinates = line.split(' ')
    x = float(coordinates[1])
    y = float(coordinates[2])
    z = float(coordinates[3])
    return (x, y, z, [])

def getP(pointO, pointG):
    H = math.sqrt((pointO[0] - pointG[0])**2 + (pointO[1] - pointG[1])**2 + (pointO[2] - pointG[2])**2)
    return np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1/H], [0, 0, 0, 0]])

def getT(pointO, pointG):
    T1 = getT1(pointO)

    x1 = pointG[0] - pointO[0]
    y1 = pointG[1] - pointO[1]
    z1 = pointG[2] - pointO[2]

    T2 = getT2((x1, y1, z1))

    x2 = math.sqrt(x1**2 + y1**2)
    y2 = 0
    z2 = z1

    T3 = getT3((x2, y2, z2))
    T4 = getT4()
    T5 = getT5()

    return T1 * T2 * T3 * T4 * T5

def getT1(pointO):
    return np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-pointO[0], -pointO[1], -pointO[2], 1]])

def getT2(pointG):
    divisor = math.sqrt(pointG[0]**2 + pointG[1]**2)
    if divisor == 0:
        return np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    sina = pointG[1] / divisor
    cosa = pointG[0] / divisor
    return np.matrix([[cosa, -sina, 0, 0], [sina, cosa, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def getT3(pointG):
    divisor = math.sqrt(pointG[0]**2 + pointG[2]**2)
    sinb = pointG[0] / divisor
    cosb = pointG[2] / divisor
    return np.matrix([[cosb, 0, sinb, 0], [0, 1, 0, 0], [-sinb, 0, cosb, 0], [0, 0, 0, 1]])

def getT4():
    return np.matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def getT5():
    return np.matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

def getPoylgons(polygons, pointO, pointG):
    realPolygons = []
    for polygon in polygons:
        pointA = polygon[0]
        pointB = polygon[1]
        pointC = polygon[2]

        vectorB = np.array([pointB[0] - pointA[0], pointB[1] - pointA[1], pointB[2] - pointA[2]])
        vectorA = np.array([pointC[0] - pointA[0], pointC[1] - pointA[1], pointC[2] - pointA[2]])

        vectorN = np.cross(vectorA, vectorB)

        vectorO = np.array([pointO[0] - pointG[0], pointO[1] - pointG[1], pointO[2] - pointG[2]])

        dotProduct = np.dot(vectorN, vectorO)

        vectorNLength = np.linalg.norm(vectorN)
        vectorOLength = np.linalg.norm(vectorO)

        angle = math.acos(dotProduct / (vectorNLength * vectorOLength))
        if angle <= (np.pi / 2):
            realPolygons.append(polygon)

    return realPolygons

def getNormal(polygon):
    pointA = polygon[0]
    pointB = polygon[1]
    pointC = polygon[2]

    centerX = (pointA[0] + pointB[0] + pointC[0]) / 3.0
    centerY = (pointA[1] + pointB[1] + pointC[1]) / 3.0
    centerZ = (pointA[2] + pointB[2] + pointC[2]) / 3.0

    vectorB = np.array([pointB[0] - pointA[0], pointB[1] - pointA[1], pointB[2] - pointA[2]])
    vectorA = np.array([pointC[0] - pointA[0], pointC[1] - pointA[1], pointC[2] - pointA[2]])

    return np.cross(vectorA, vectorB)

def getBrightness(point, pointI):

    vectorL = np.array([pointI[0] - point[0], pointI[1] - point[1], pointI[2] - point[2]])
    vectorN = sum(point[3]) / len(point[3])

    dotProduct = np.dot(vectorL, vectorN)

    vectorLLength = np.linalg.norm(vectorL)
    vectorNLength = np.linalg.norm(vectorN)

    LN = dotProduct / (vectorLLength * vectorNLength)

    return destinationIntensity * ka + sourceIntensity * kd * LN

file = open('teapot.obj', 'r')
# file = open('kocka.obj', 'r')

vertices = []
polygons = []

for line in file:
    if line.startswith('o'):
        pointO = serializeLine(line)

    if line.startswith('i'):
        pointI = serializeLine(line)

    if line.startswith('g'):
        pointG = serializeLine(line)

    if line.startswith('v'):
        vertice = serializeLine(line)
        vertices.append(vertice)

file.seek(0)
for line in file:
    if line.startswith('f'):
        coordinates = line.split(' ')
        v1 = int(coordinates[1])
        v2 = int(coordinates[2])
        v3 = int(coordinates[3])
        normal = getNormal((vertices[v1 - 1], vertices[v2 - 1], vertices[v3 - 1]))
        vertices[v1 - 1][3].append(normal)
        vertices[v2 - 1][3].append(normal)
        vertices[v3 - 1][3].append(normal)

        polygon = (vertices[v1 - 1], vertices[v2 - 1], vertices[v3 - 1])
        polygons.append(polygon)

realPoylgons = getPoylgons(polygons, pointO, pointG);

T = getT(pointO, pointG)
P = getP(pointO, pointG)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    for polygon in realPoylgons:
        glBegin(GL_TRIANGLES)
        for point in polygon:
            brightness = getBrightness(point, pointI)
            newPoint = transform(point, T, P)
            glColor3f(brightness, brightness, brightness)
            glVertex2f(newPoint[0, 0], newPoint[0, 1])
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
gluOrtho2D(-5.0, 5.0, -5.0, 5.0) #kocka i teapot
glutDisplayFunc(display)
glutMainLoop()
