from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

bresenhamOffset = 0.005

def line(x1, y1, x2, y2, z):
  a = (y2-y1)/(x2-x1)
  x = x1
  while x <= x2:
    x+=bresenhamOffset
    y = (y1 + a * (x - x1))
    # print(x,y)
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(x,y,z)
    glEnd()

def lineXtoZ(x1, z1, x2, z2, y):
  a = (z2-z1)/(x2-x1)
  x = x1
  while x <= x2:
    x+=0.00005
    z = (z1 + a * (x - x1))
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(x,y,z)
    glEnd()
