from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
from PIL import Image
from readTexture import *

def drawGround():
  texture_0 = read_texture('./src/grass.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)

  glTexCoord2f(0.0, 20.0); glVertex3f(-0.75, 2.0, 0.05)
  glTexCoord2f(20.0, 0.0); glVertex3f(-0.75, 2.0, 16.0)
  glTexCoord2f(0.0, 0.0); glVertex3f(3.75, 2.0, 16.0)
  glTexCoord2f(20.0, 20.0); glVertex3f(3.75, 2.0, 0.05)

  glTexCoord2f(0.0, 20.0); glVertex3f(2.3, 2.035, 1.4)
  glTexCoord2f(20.0, 0.0); glVertex3f(2.3, 2.035, 1.905) 
  glTexCoord2f(0.0, 0.0); glVertex3f(1.11, 2.035, 1.905) 
  glTexCoord2f(20.0, 20.0); glVertex3f(1.11, 2.035, 1.4)

  glEnd()
  glDisable(GL_TEXTURE_2D)
