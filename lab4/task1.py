from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def transform(point, dx, dy, scale):
    x = point[0] - dx;
    y = point[1] - dy;
    return (x * scale, y * scale)

file = open('kocka.obj', 'r')

vertices = []
xs = []
ys = []
zs = []
polygons = []

for line in file:
    if line.startswith('v'):
        coordinates = line.split(' ')
        x = float(coordinates[1])
        y = float(coordinates[2])
        z = float(coordinates[3])
        vertices.append((x, y, z))
        xs.append(x)
        ys.append(y)
        zs.append(z)

xmin = min(xs)
ymin = min(ys)
xmax = max(xs)
ymax = max(ys)

file.seek(0)
for line in file:
    if line.startswith('f'):
        coordinates = line.split(' ')
        v1 = int(coordinates[1])
        v2 = int(coordinates[2])
        v3 = int(coordinates[3])
        polygons.append((vertices[v1 - 1], vertices[v2 - 1], vertices[v3 - 1]))

input = raw_input('Molim koordinate tocke: ')
coordinates = input.split(' ')
xT = float(coordinates[0])
yT = float(coordinates[1])
zT = float(coordinates[2])

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    scale = 200.0 / max(xmax-xmin, ymax-ymin)
    outside = False
    for polygon in polygons:
        x = polygon[0]
        y = polygon[1]
        z = polygon[2]

        A = (y[1] - y[0]) * (z[2] - z[0]) - (z[1] - z[0]) * (y[2] - y[0])
        B = -(x[1] - x[0]) * (z[2] - z[0]) + (z[1] - z[0]) * (x[2] - x[0])
        C = (x[1] - x[0]) * (y[2] - y[0]) - (y[1] - y[0]) * (x[2] - x[0])
        D = -x[0] * A - y[0] * B - z[0] * C

        outside = outside or (A * xT + B * yT + C * zT + D > 0)

        glBegin(GL_POLYGON)
        for point in polygon:
            newPoint = transform(point, xmin, ymin, scale)
            glVertex2f(newPoint[0], newPoint[1])
        glEnd()

    if outside:
        print 'TOCKA V JE IZVAN POLIGONA!'
    else:
        print 'TOCKA V JE UNUTAR POLIGONA!'
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(200, 200)
glutInitWindowPosition(0, 0)
glutCreateWindow('Dots_are_line')
glClearColor(0.0,0.0,0.0,0.0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0.0, 200.0, 0.0, 200.0)
glutDisplayFunc(display)
glutMainLoop()
