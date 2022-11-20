from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from readTexture import *

total = 10
color = [0.0, 0.7, 0.7]

def drawGrandStandLeft():
  bricks = read_texture('./src/ground-gray.jpg')
  glEnable(GL_TEXTURE_2D)
  glEnable(GL_COLOR_MATERIAL)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, 16.0)
    glTexCoord2f(20.0, 0.0); glVertex3f(-5.0 + xOffset, 5.0 - yOffset, -4.4)
    glTexCoord2f(20.0, 20.0); glVertex3f(-5.0 + xOffset, 3.0 - yOffset, -4.4)
    glTexCoord2f(0.0, 20.0); glVertex3f(-5.0 + xOffset, 3.0 - yOffset, 16.0)

    glVertex3f(-5.0 + xOffset, 5.0 - yOffset, 16.0)
    glVertex3f(-5.0 + xOffset, 5.0 - yOffset, -4.4)
    glVertex3f(-5.5 + xOffset, 5.0 - yOffset, -4.4)
    glVertex3f(-5.5 + xOffset, 5.0 - yOffset, 16.0)
    
  glEnd()
  glDisable(GL_TEXTURE_2D)


def drawGrandStandRight():
  for i in range(0, total):
    xOffset = 0.5 * i
    yOffset = 0.25 * i
    glPushMatrix()
    glTranslatef(8-xOffset, 2.0 - yOffset, 2.0)
    glScalef(0.5, 4.0, 16.0)
    glEnable(GL_COLOR_MATERIAL)
    glColor3f(color[0], color[1], color[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glPopMatrix()

def drawGrandStandTop():
  bricks = read_texture('./src/ground-gray.jpg')

  glEnable(GL_TEXTURE_2D)
  glBegin(GL_QUADS)
  for i in range(0, total):
    xOffset = 0
    zOffset = 0.5 * i
    yOffset = 0.25 * i

    glTexCoord2f(0.0, 0.0); glVertex3f(-5.1, 5.0 -yOffset, -4.45 + zOffset)
    glTexCoord2f(20.0, 0.0); glVertex3f(-5.1, 3.0 -yOffset, -4.45+ zOffset)
    glTexCoord2f(20.0, 20.0); glVertex3f(5.0, 3.0 -yOffset, -4.45+ zOffset)
    glTexCoord2f(0.0, 20.0); glVertex3f(5.0, 5.0 -yOffset, -4.45 + zOffset)

    glVertex3f(-5.1, 5.0 - yOffset, -5.5 + zOffset)
    glVertex3f(-5.1, 5.0 - yOffset, -4.45 + zOffset)
    glVertex3f(5.0, 5.0 - yOffset, -5.5 + zOffset)
    glVertex3f(5.0, 5.0 - yOffset, -4.45 + zOffset)
    
  glEnd()
  glDisable(GL_TEXTURE_2D)
  # for i in range(0, total):
  #   xOffset = 0
  #   zOffset = 0.5 * i
  #   yOffset = 0.25 * i
  #   glPushMatrix()
  #   glTranslatef(2, 2.0 - yOffset, -4.2 + zOffset)
  #   glScalef(12, 4.0, 0.5)
  #   glEnable(GL_COLOR_MATERIAL)
  #   glColor3f(color[0], color[1], color[2])
  #   glutSolidCube(1.0)

  #   mat_specular = [0.0, 0.0, 0.0]
  #   mat_shininess = [0.0]
  #   glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  #   glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  #   glPopMatrix()