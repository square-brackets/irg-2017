"""
Kratak opis programa/potprograma i medjusobnu povezanost:
    - Usporediti crtanje linije koristeci Bresenham-ovim postupkom i koristeci LINE naredbu
Promjene nacinjene s obzirom na upute:
    - Dodana je provjera ukoliko je nagib pravca veci od 45 stupnjeva, te se parametri primaju kao argumenti
Koristene strukture podataka:
    -
Upute za koristenje programa:
    - Program se pokrece pozivom naredbe `python lab2/task1.py` s odgovarajucim argumentima, primjer: `python lab2/task1.py 10 10 200 100`
Komentar rezultata (brzina, moguce promjene, problemi, nedostaci):
    - Posto je radi o samo iscrtavanju jedne linije nisu se primijetile ikakvi padovi performansi.

# Dodatni resurs:   https://alala666888.wordpress.com/2010/06/06/opengl2d-draw-points-and-lines/
                    http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm
"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

# filename + 4 values
if not len(sys.argv) == 5:
    raise BaseException('Nedovoljan broj argumenata')

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    start = (int(sys.argv[1]), int(sys.argv[2]))
    end = (int(sys.argv[3]), int(sys.argv[4]))

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    x0 = x2 - x1
    y0 = y2 - y1
    if not x0 == 0:
        steep = y0/float(x0)
    else:
        steep = 999999999999
    D = steep - 0.5

    x = start[0]
    y = start[1]

    isSteep = abs(y0) > abs(x0)

    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    x0 = x2 - x1
    y0 = y2 - y1

    glBegin(GL_POINTS)

    for x in range(x1, x2 + 1):
        if isSteep:
            glVertex2i(y,x)
        else:
            glVertex2i(x,y)

        D -= abs(y0)
        if D < 0:
            y += 1
            D += x0

    glEnd()

    glBegin(GL_LINES)
    glVertex2i(start[0], start[1] + 20)
    glVertex2i(end[0], end[1] + 20)
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
