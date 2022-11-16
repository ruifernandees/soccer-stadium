from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawGround(wallWidth, wallHeight, wallDepth):
  glTranslatef(wallWidth/3, wallHeight/2 , (wallDepth/2) )
  glScalef(wallWidth, wallHeight, wallDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(0.0, 0.5, 0.2)
  glutSolidCube(1.0)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
