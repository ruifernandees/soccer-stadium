from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from readTexture import *

total = 10
color = [0.0, 0.7, 0.7]

def drawGrandStandLeft():
  bricks = read_texture('./src/ground-gray.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, 16.0)
    glTexCoord2f(100.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(100.0, 100.0); glVertex3f(-5.0 + xOffset, 3.0 - yOffset, -4.4)
    glTexCoord2f(0.0, 100.0); glVertex3f(-5.0 + xOffset, 3.0 - yOffset, 16.0)

  glEnd()
  glDisable(GL_TEXTURE_2D)

  bricks = read_texture('./src/texture-green.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i
    glTexCoord2f(0.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, 16.0)
    glTexCoord2f(100.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(100.0, 100.0); glVertex3f(-5.5 + xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(0.0, 100.0); glVertex3f(-5.5 + xOffset, 5.0 - yOffset, 16.0)

  glEnd()
  glDisable(GL_TEXTURE_2D)
    


def drawGrandStandRight():
  bricks = read_texture('./src/ground-gray.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(8.5 - xOffset, 5.0 - yOffset, 16.0)
    glTexCoord2f(100.0, 0.0); glVertex3f(8.5 - xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(100.0, 100.0); glVertex3f(8.5 - xOffset, 3.0 - yOffset, -4.4)
    glTexCoord2f(0.0, 100.0); glVertex3f(8.5 - xOffset, 3.0 - yOffset, 16.0)

  glEnd()
  glDisable(GL_TEXTURE_2D)

  bricks = read_texture('./src/texture-green.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i
    glTexCoord2f(0.0, 0.0); glVertex3f(9.0 - xOffset, 5.0 - yOffset, 16.0)
    glTexCoord2f(100.0, 0.0); glVertex3f(9.0 - xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(100.0, 100.0); glVertex3f(8.5 - xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(0.0, 100.0); glVertex3f(8.5 - xOffset, 5.0 - yOffset, 16.0)

  glEnd()
  glDisable(GL_TEXTURE_2D)

def drawGrandStandTop():
  bricks = read_texture('./src/ground-gray.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0
    zOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(-5.1, 5.0 -yOffset, -4.45 + zOffset)
    glTexCoord2f(100.0, 0.0); glVertex3f(-5.1, 3.0 -yOffset, -4.45+ zOffset)
    glTexCoord2f(100.0, 100.0); glVertex3f(10.0, 3.0 -yOffset, -4.45+ zOffset)
    glTexCoord2f(0.0, 100.0); glVertex3f(10.0, 5.0 -yOffset, -4.45 + zOffset)

  glEnd()
  glDisable(GL_TEXTURE_2D)

  bricks = read_texture('./src/texture-green.jpg')
  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0
    zOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(-5.1, 5.0 - yOffset, -5.5 + zOffset)
    glTexCoord2f(100.0, 0.0); glVertex3f(-5.1, 5.0 - yOffset, -4.45 + zOffset)
    glTexCoord2f(100.0, 100.0); glVertex3f(10.0, 5.0 - yOffset, -5.5 + zOffset)
    glTexCoord2f(0.0, 100.0); glVertex3f(10.0, 5.0 - yOffset, -4.45 + zOffset)
    

  glEnd()
  glDisable(GL_TEXTURE_2D)
