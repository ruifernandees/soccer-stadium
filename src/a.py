import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy
from PIL import Image

def read_texture(filename):
  img = Image.open(filename)
  img_data = numpy.array(list(img.getdata()), numpy.int8)
  textID = glGenTextures(1)
  glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
  glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
  glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
  return textID

def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0)
  texture_0 = read_texture('./src/imagem.bmp')
  glEnable(GL_TEXTURE_2D)
  glBindTexture(GL_TEXTURE_2D,texture_0)
  glBegin(GL_QUADS)
  glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
  glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
  glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
  glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
  # POSTERIOR
  glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
  glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
  glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
  glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
  # Face superior
  glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
  glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0);
  glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0);
  glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
  # Face inferior
  glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0);
  glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0);
  glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
  glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
  # Face lateral direita
  glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
  glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
  glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
  glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
  # Face lateral esquerda
  glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
  glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
  glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
  glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
  
  # glTexCoord2f(0.0,0.0)
  # glVertex3f(-0.5, -0.5, 0.0)
  # glTexCoord2f(1.0,0.0)
  # glVertex3f(0.5, -0.5, 0.0)
  # glTexCoord2f(0.0,1.0)
  # glVertex(0.5, 0.5, 0.0)
  # glTexCoord2f(0.0,1.0)
  # glVertex(-0.5, 0.5, 0.0)
  glEnd()
  glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutCreateWindow("oldgl")
glutDisplayFunc(display)
glutMainLoop()