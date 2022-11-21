from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawLightSupport(mode = 'left'):
  glPushMatrix()
  goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth = 0.03, 1.67, 0.03
  if (mode == 'left'):
    glTranslatef(-5.1, 4.5 , -5.0 )
  elif (mode == 'right'):
    glTranslatef(7.5, 4.5 , -5.0 )

  glScalef(goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(1, 1, 1)
  glutSolidCube(1.0)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glPopMatrix()

def drawLightCube(mode = 'left'):
  glPushMatrix()
  goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth = 1, 1, 0.03
  if (mode == 'left'):
    glTranslatef(-5.1, 5.5 , -5.0 )
    glRotatef(20.0, 0, 1,0)
  elif (mode == 'right'):
    glTranslatef(7.4, 5.5 , -5.0 )
    glRotatef(-20.0, 0, 1,0 )

  glScalef(goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(1, 1, 1)
  glutSolidCube(1.0)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  # if (not isDay):
  #   if (mode == 'left'):
  #     glLightfv(GL_LIGHT0, GL_POSITION , [-5.1, 5.5 , -3.0], 3 )
  #   elif (mode == 'right'):
  #     glLightfv(GL_LIGHT0, GL_POSITION, [7.5, 5.5 , -3.0], 4 )
  glPopMatrix()