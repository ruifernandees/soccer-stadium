from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from bresenham import *

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
    offset = 0.001
    x = 0
    y = r
    CirclePlotPoints(x_centre, y_centre, x, y, z)

    D = 3 - 2 * r

    glColor3f(0.0, 1.0, 0.5)
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


# def CirclePlotPointsXZ(x_centre, z_centre, x, y, z):
#     glVertex3f(x_centre + x, y, x_centre + z)
#     glVertex3f(x_centre - x, y, z_centre + z)
#     glVertex3f(x_centre + x, y, z_centre - z)
#     glVertex3f(x_centre - x, y, z_centre - z)
#     glVertex3f(x_centre + z, y, z_centre + x)
#     glVertex3f(x_centre - z, y, z_centre + x)
#     glVertex3f(x_centre + z, y, z_centre - x)
#     glVertex3f(x_centre - z, y, z_centre - x)


# def BresenhamCircleDrawXZ(x_centre, y_centre, z_centre, r):
#     x = 0
#     z = r
#     CirclePlotPointsXZ(x_centre, z_centre, x, y_centre, z)

#     D = 3 - 2 * r

#     glColor3f(0.0, 1.0, 0.5)
#     glPointSize(3.0)
#     glBegin(GL_POINTS)

#     while x <= z:

#         if D < 0:
#             D = D + 4 * x + 2

#         else:
#             z -= 1
#             D = D + 4 * (x - z) + 2

#         CirclePlotPointsXZ(x_centre, z_centre, x, y_centre, z)
#         x += 1

#     glEnd()
#     glFlush()

# def CirclePlotPointsXY(x_centre, y_centre, x, y, z):
#     glVertex3f(x_centre + x, x_centre + y, z)
#     glVertex3f(x_centre - x, y_centre + y, z)
#     glVertex3f(x_centre + x, y_centre - y, z)
#     glVertex3f(x_centre - x, y_centre - y, z)
#     glVertex3f(x_centre + y, y_centre + x, z)
#     glVertex3f(x_centre - y, y_centre + x, z)
#     glVertex3f(x_centre + y, y_centre - x, z)
#     glVertex3f(x_centre - y, y_centre - x, z)


# def BresenhamCircleDrawXY(x_centre, y_centre, z_centre, r):
#     x = 0
#     y = r
#     CirclePlotPointsXY(x_centre, y_centre, x, y, z_centre)

#     D = 3 - 2 * r

#     glColor3f(0.0, 1.0, 0.5)
#     glPointSize(3.0)
#     glBegin(GL_POINTS)

#     while x <= y:

#         if D < 0:
#             D = D + 4 * x + 2

#         else:
#             y -= 1
#             D = D + 4 * (x - y) + 2

#         CirclePlotPointsXY(x_centre, y_centre, x, y, z_centre)
#         x += 1

#     glEnd()
#     glFlush()


def drawGroundLines():
  # lineX, lineY, lineZ = 0.0, 1, 0.0
  xOffset = 0.1
  zOffset = 0.6

  x, y, z, r = 1.1 + xOffset, 2.0, 5.0 + zOffset, 2.0
  BresenhamCircleDraw(x, y, r, z)

  #TOP
  line(0.0 + xOffset, 2.0, 3.0 + xOffset, 2.0, 0.0 + zOffset)

  #RIGHT
  lineXtoZ(3.0 + xOffset, 0.0 + zOffset, 3.1 + xOffset, 10.0 + zOffset, 2.0)

  #LEFT
  lineXtoZ(0.0 + xOffset, 0.0 + zOffset, 0.1 + xOffset, 10.0 + zOffset, 2.0)

  # BOTTOM 
  line(0.1 + xOffset, 2.0, 3.1 + xOffset, 2.0, 10.0 + zOffset)

  # CENTER 
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.0 + zOffset)
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.001 + zOffset)
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.002 + zOffset)


#   BresenhamCircleDraw(x, y+0.4, z, r)

  # # CIRCLE CENTER
  # total = 10
  # initialX = 1.50 + xOffset
  # initialY = 2.0 + xOffset
  # initialZ = 4.0 + zOffset
  # line(1.50 + xOffset, 2.0, 1.6 + xOffset, 2.0, 4.0 + zOffset)
  # for i in range(0, total):
  #   currentXOffset = initialX * i 
  #   currentYOffset = initialY * i 
  #   currentZOffset = initialZ * i 
  #   lineXtoZ(1.60 + currentXOffset, 4.0 + currentZOffset, 1.65 + currentXOffset, 4.05 + currentZOffset, 2.0)
  # # lineXtoZ(1.65 + xOffset, 4.05 + zOffset, 1.66 + xOffset, 4.10 + zOffset, 2.0)
  # # lineXtoZ(1.651 + xOffset, 4.20 + zOffset, 1.60 + xOffset, 4.25 + zOffset, 2.0)
  # # lineXtoZ(1.651 + xOffset, 4.20 + zOffset, 1.60 + xOffset, 4.25 + zOffset, 2.0)

  # PEQUENA AREA - AZUL
  lineXtoZ(2.1 + xOffset, 0.0 + zOffset, 2.105 + xOffset, 0.7 + zOffset, 2.0)
  lineXtoZ(1.0 + xOffset, 0.0 + zOffset, 1.005 + xOffset, 0.7 + zOffset, 2.0)
  line(1.0 + xOffset, 2.0, 2.1 + xOffset, 2.0, 0.7 + zOffset)

  # GRANDE AREA - AZUL
  lineXtoZ(2.4 + xOffset, 0.0 + zOffset, 2.405 + xOffset, 1.3 + zOffset, 2.0)
  lineXtoZ(0.7 + xOffset, 0.0 + zOffset, 0.705 + xOffset, 1.3 + zOffset, 2.0)
  line(0.7 + xOffset, 2.0, 2.4 + xOffset, 2.0, 1.3 + zOffset)

  # PEQUENA AREA - VERMELHO
  lineXtoZ(2.1 + xOffset, 9.3 + zOffset, 2.105 + xOffset, 10 + zOffset, 2.0)
  lineXtoZ(1.0 + xOffset, 9.3 + zOffset, 1.005 + xOffset, 10 + zOffset, 2.0)
  line(1.0 + xOffset, 2.0, 2.1 + xOffset, 2.0, 9.3 + zOffset)

  # GRANDE AREA - VERMELHO
  lineXtoZ(2.4 + xOffset, 8.7 + zOffset, 2.405 + xOffset, 10 + zOffset, 2.0)
  lineXtoZ(0.7 + xOffset, 8.7 + zOffset, 0.705 + xOffset, 10 + zOffset, 2.0)
  line(0.7 + xOffset, 2.0, 2.4 + xOffset, 2.0, 8.7 + zOffset)
