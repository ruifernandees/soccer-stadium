from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
from PIL import Image
from readTexture import *

def drawGround(cameraZ):
  texture_0 = read_texture('./src/grass.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)

  glTexCoord2f(0.0, 20.0); glVertex3f(-0.75, 2.0, 0.05)
  glTexCoord2f(20.0, 0.0); glVertex3f(-0.75, 2.0, 16.0)
  glTexCoord2f(0.0, 0.0); glVertex3f(3.75, 2.0, 16.0)
  glTexCoord2f(20.0, 20.0); glVertex3f(3.75, 2.0, 0.05)

  if (cameraZ >= 7.699):
    zFinal = 1.905
  elif (cameraZ < 7.699 and cameraZ >= 3.11):
    zFinal = 1.925
  else:
    zFinal = 1.90

  glTexCoord2f(0.0, 20.0); glVertex3f(1.11, 2.035, 1.4)
  glTexCoord2f(20.0, 0.0); glVertex3f(1.11, 2.035, zFinal) 
  glTexCoord2f(0.0, 0.0); glVertex3f(2.3, 2.035, zFinal) 
  glTexCoord2f(20.0, 20.0); glVertex3f(2.3, 2.035, 1.4)

  if (cameraZ >= 12.5):
    zFinal = 9.38
  elif (cameraZ < 12.5 and cameraZ >= 11.6):
    zFinal = 9.36
  else:
    zFinal = 9.35
  glTexCoord2f(0.0, 20.0); glVertex3f(2.3, 2.035, 9.9)
  glTexCoord2f(20.0, 0.0); glVertex3f(2.3, 2.035, zFinal) 
  glTexCoord2f(0.0, 0.0); glVertex3f(1.11, 2.035, zFinal) 
  glTexCoord2f(20.0, 20.0); glVertex3f(1.11, 2.035, 9.9)

  glEnd()
  glDisable(GL_TEXTURE_2D)
