from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawMoon(isDay):
  if (isDay):
    return False
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  moonColor = [1, 1, 1]
  glColor3f(moonColor[0], moonColor[1], moonColor[2])
  glTranslatef(-2, 18.0, -40)
  glutSolidSphere(0.4, SLICES, STACKS)
  mat_specular = [1, 1, 1]
  mat_shininess = [1.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)