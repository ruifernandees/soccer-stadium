from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawSky(isDay ):
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  skyColor = []
  if (isDay):
    skyColor = [0.53, 0.81, 0.92]
  else:
    skyColor = [0.1, 0.1, 0.1]
  glColor3f(skyColor[0], skyColor[1], skyColor[2])
  glTranslatef(0, 0, 0)
  glutSolidSphere(50, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)