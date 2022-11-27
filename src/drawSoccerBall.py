from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawSoccerBall(soccerBallX, soccerBallY, soccerBallZ, soccerBallRotationX, soccerBallRotationY, soccerBallRotationZ):
  glPushMatrix()
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  ballColor = [1, 1, 1]
  glColor3f(ballColor[0], ballColor[1], ballColor[2])
  glTranslatef(soccerBallX, soccerBallY, soccerBallZ)
  glRotatef(soccerBallRotationY, 0.0, 1.0, 0.0)
  glRotatef(soccerBallRotationZ, 0.0, 0.0, 1.0)
  glRotatef(soccerBallRotationX, 1.0, 0.0, 0.0)
  glutWireSphere(0.022, SLICES, STACKS)
  glutSolidSphere(0.022, SLICES, STACKS)
  glColor3f(0, 0, 0)
  glutSolidCube(0.031)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glPopMatrix()