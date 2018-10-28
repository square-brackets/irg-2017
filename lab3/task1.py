from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

# 1.
verticesNum = input('Molim broj vrhova poligona: ')
vertices = []

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    # 2.
    xs = []
    ys = []
    for i in range(verticesNum):
        input = raw_input('Molim koordinate vrha: ')
        coordinates = input.split(' ')
        x = int(coordinates[0])
        y = int(coordinates[1])
        xs.append(x)
        ys.append(y)
        vertices.append((x, y))

    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)

    # 3.
    vertices.append(vertices[0])
    xs.append(vertices[0][0])
    ys.append(vertices[0][1])

    # 4.
    glBegin(GL_LINE_LOOP)
    for point in vertices:
        glVertex2i(point[0], point[1])
    glEnd()

    # 5.
    a = []
    for i in range(verticesNum):
        a.append(ys[i] - ys[i + 1])

    b = []
    for i in range(verticesNum):
        b.append(-xs[i] + xs[i + 1])

    c = []
    for i in range(verticesNum):
        c.append(xs[i] * ys[i + 1] - xs[i + 1] * ys[i])

    # 6.
    input = raw_input('Molim koordinate tocke: ')
    coordinates = input.split(' ')
    x1 = int(coordinates[0])
    y1 = int(coordinates[1])

    # 7.
    isOut = False
    for i in range(verticesNum):
        isOut = isOut or (x1 * a[i] + y1 * b[i] + c[i] > 0)
        if isOut:
            break

    if isOut:
        print 'TOCKA V JE IZVAN POLIGONA!'
    else:
        print 'TOCKA V JE UNUTAR POLIGONA!'

    # 8.
    for y0 in range(ymin, ymax):

        # 9.
        L = xmin
        D = xmax

        # 10.
        for i in range(verticesNum):

            # 11.
            if a[i] == 0:
                continue

            # 12.
            x1 = (-b[i] * y0 - c[i]) / float(a[i])

            # 13.
            if ys[i] < ys[i + 1] and x1 > L:
                L = x1

            # 14.
            if ys[i] >= ys[i + 1] and x1 < D:
                D = x1

        # 15.
        if L < D:
            glBegin(GL_LINES)
            glVertex2f(L, float(y0))
            glVertex2f(D, float(y0))
            glEnd()

    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow('Dots_are_line')
glClearColor(0.0,0.0,0.0,0.0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0.0, 200.0, 0.0, 150.0)
glutDisplayFunc(display)
glutMainLoop()

print vertices
