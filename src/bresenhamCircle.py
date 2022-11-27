from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def CirclePlotPointsXZ(x_centre, z_centre, x, y, z):
    glVertex3f(x_centre + x, y, z_centre + z)
    glVertex3f(x_centre - x, y, z_centre + z)
    glVertex3f(x_centre + x, y, z_centre - z)
    glVertex3f(x_centre - x, y, z_centre - z)
    glVertex3f(x_centre + z, y, z_centre + x)
    glVertex3f(x_centre - z, y, z_centre + x)
    glVertex3f(x_centre + z, y, z_centre - x)
    glVertex3f(x_centre - z, y, z_centre - x)


def BresenhamCircleDrawXZ(x_centre, z_centre, r, y):
    glPushMatrix()
    offset = 0.001
    x = 0
    z = r
    CirclePlotPointsXZ(x_centre, z_centre, x, y, z)

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

        CirclePlotPointsXZ(x_centre, z_centre, x, y, z)
        x += offset

    glEnd()
    glFlush()
    glPopMatrix()

def CirclePlotPoints(x_centre, y_centre, x, y, z):
    glVertex3f(x_centre + x, y_centre + y, z)
    glVertex3f(x_centre - x, y_centre + y, z)
    glVertex3f(x_centre + x, y_centre - y, z)
    glVertex3f(x_centre - x, y_centre - y, z)
    glVertex3f(x_centre + y, y_centre + x, z)
    glVertex3f(x_centre - y, y_centre + x, z)
    glVertex3f(x_centre + y, y_centre - x, z)
    glVertex3f(x_centre - y, y_centre - x, z)


def BresenhamCircleDraw(x_centre, y_centre, r, z):
    glPushMatrix()
    glRotate(90, 0,0,1)
    offset = 0.001
    x = 0
    y = r
    CirclePlotPoints(x_centre, y_centre, x, y, z)

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

        CirclePlotPoints(x_centre, y_centre, x, y, z)
        x += offset

    glEnd()
    glFlush()
    glPopMatrix()
