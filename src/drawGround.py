from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
from PIL import Image

def drawGround(wallWidth, wallHeight, wallDepth):
  glPushMatrix()
  # texture = glGenTextures(1)
  # glBindTexture(GL_TEXTURE_2D, texture)
  # # set the texture wrapping/filtering options (on the currently bound texture object)
  # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)	
  # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
  # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
  # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
  # img = Image.open('./src/tex-blue.jpg')
  # img_data = numpy.array(list(img.getdata()), numpy.int8)
  # textID = glGenTextures(1)
  # glBindTexture(GL_TEXTURE_2D,textID)
  # glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
  # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 200, 150, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
  # glGenerateMipmap(GL_TEXTURE_2D)
  glTranslatef(wallWidth/3, wallHeight/2 , (wallDepth/2) )
  glScalef(wallWidth, wallHeight, wallDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(0.0, 0.5, 0.2)
  # glEnable(GL_TEXTURE_GEN_S) #enable texture coordinate generation
  # glEnable(GL_TEXTURE_GEN_T)
  # glBindTexture(GL_TEXTURE_2D, textID)
  # glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
  glutSolidCube(1)
  # glDisable(GL_TEXTURE_GEN_S) #enable texture coordinate generation
  # glDisable(GL_TEXTURE_GEN_T)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glPopMatrix()
