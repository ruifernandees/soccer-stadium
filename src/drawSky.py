from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawSky():
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  skyBlue = [0.53, 0.81, 0.92]
  glColor3f(skyBlue[0], skyBlue[1], skyBlue[2])
  glTranslatef(0, 0, 0)
  glutSolidSphere(50, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)