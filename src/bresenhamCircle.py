from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def CirclePlotPointsXZ(xc, zc, x, y, z):
    glVertex3f(xc + x, y, zc + z)
    glVertex3f(xc - x, y, zc + z)
    glVertex3f(xc + x, y, zc - z)
    glVertex3f(xc - x, y, zc - z)
    glVertex3f(xc + z, y, zc + x)
    glVertex3f(xc - z, y, zc + x)
    glVertex3f(xc + z, y, zc - x)
    glVertex3f(xc - z, y, zc - x)


def BresenhamCircleDrawXZ(xc, zc, r, y):
    offset = 0.001
    x = 0
    z = r
    CirclePlotPointsXZ(xc, zc, x, y, z)

    D = 3 - 2 * r

    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)

    while x <= z:

        if D < 0:
            D = D + 4 * x + 2

        else:
            z -= offset
            D = D + 4 * (x - y) + 2

        CirclePlotPointsXZ(xc, zc, x, y, z)
        x += offset

    glEnd()
    glFlush()

def CirclePlotPoints(xc, yc, x, y, z):
    glVertex3f(xc + x, yc + y, z)
    glVertex3f(xc - x, yc + y, z)
    glVertex3f(xc + x, yc - y, z)
    glVertex3f(xc - x, yc - y, z)
    glVertex3f(xc + y, yc + x, z)
    glVertex3f(xc - y, yc + x, z)
    glVertex3f(xc + y, yc - x, z)
    glVertex3f(xc - y, yc - x, z)


def BresenhamCircleDraw(xc, yc, r, z):
    glPushMatrix()
    glRotate(90, 0,0,1)
    offset = 0.001
    x = 0
    y = r
    CirclePlotPoints(xc, yc, x, y, z)

    D = 3 - 2 * r

    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)

    while x <= y:

        if D < 0:
            D = D + 4 * x + 2

        else:
            y -= offset
            D = D + 4 * (x - y) + 2

        CirclePlotPoints(xc, yc, x, y, z)
        x += offset

    glEnd()
    glFlush()
    glPopMatrix()
