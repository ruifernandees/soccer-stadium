from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawGrandStandLeft(color = [0.5, 0.5, 0.5]):
  total = 8
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i
    glPushMatrix()
    glTranslatef(-5.0+xOffset, 2.0 - yOffset, 2.0)
    glScalef(0.5, 4.0, 16.0)
    glEnable(GL_COLOR_MATERIAL)
    glColor3f(color[0], color[1], color[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPopMatrix()

def drawGrandStandRight(color = [0.5, 0.5, 0.5]):
  total = 8
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i
    glPushMatrix()
    glTranslatef(8-xOffset, 2.0 - yOffset, 2.0)
    glScalef(0.5, 4.0, 16.0)
    glEnable(GL_COLOR_MATERIAL)
    glColor3f(color[0], color[1], color[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPopMatrix()