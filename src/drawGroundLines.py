from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from bresenham import *
from bresenhamCircle import *


def drawGroundLines():
  # lineX, lineY, lineZ = 0.0, 1, 0.0
  xOffset = 0.1
  zOffset = 0.6

  central_circle_x, central_circle_y, central_circle_z, central_circle_r = 1.5 + xOffset, 2.0, 5.0 + zOffset, 0.3
  BresenhamCircleDrawXZ(central_circle_x, central_circle_z, central_circle_r, central_circle_y)

  half_moon_blue_x, half_moon_blue_y, half_moon_blue_z, half_moon_blue_r = 1.5 + xOffset, 2.0, 1.4 + zOffset, 0.5
#   glPushMatrix()
#   glTranslatef(0, -0.4, 0)
#   glRotatef(20, 0, 1, 0)
#   glRotatef(20, 0, 0, 1)
#   glRotatef(180, 1, 0, 0)
  BresenhamCircleDrawXZ(half_moon_blue_x, half_moon_blue_z, half_moon_blue_r, half_moon_blue_y)
#   glPopMatrix()

  #TOP
  line(0.0 + xOffset, 2.0, 3.0 + xOffset, 2.0, 0.0 + zOffset)

  #RIGHT
  lineXtoZ(3.0 + xOffset, 0.0 + zOffset, 3.1 + xOffset, 10.0 + zOffset, 2.0)

  #LEFT
  lineXtoZ(0.0 + xOffset, 0.0 + zOffset, 0.1 + xOffset, 10.0 + zOffset, 2.0)

  # BOTTOM 
  line(0.1 + xOffset, 2.0, 3.1 + xOffset, 2.0, 10.0 + zOffset)

  # CENTER 
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.0 + zOffset)
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.001 + zOffset)
  line(0.1 + xOffset, 2.0, 3.0 + xOffset, 2.0, 5.002 + zOffset)


#   BresenhamCircleDraw(x, y+0.4, z, r)

  # # CIRCLE CENTER
  # total = 10
  # initialX = 1.50 + xOffset
  # initialY = 2.0 + xOffset
  # initialZ = 4.0 + zOffset
  # line(1.50 + xOffset, 2.0, 1.6 + xOffset, 2.0, 4.0 + zOffset)
  # for i in range(0, total):
  #   currentXOffset = initialX * i 
  #   currentYOffset = initialY * i 
  #   currentZOffset = initialZ * i 
  #   lineXtoZ(1.60 + currentXOffset, 4.0 + currentZOffset, 1.65 + currentXOffset, 4.05 + currentZOffset, 2.0)
  # # lineXtoZ(1.65 + xOffset, 4.05 + zOffset, 1.66 + xOffset, 4.10 + zOffset, 2.0)
  # # lineXtoZ(1.651 + xOffset, 4.20 + zOffset, 1.60 + xOffset, 4.25 + zOffset, 2.0)
  # # lineXtoZ(1.651 + xOffset, 4.20 + zOffset, 1.60 + xOffset, 4.25 + zOffset, 2.0)

  # PEQUENA AREA - AZUL
  lineXtoZ(2.1 + xOffset, 0.0 + zOffset, 2.105 + xOffset, 0.7 + zOffset, 2.0)
  lineXtoZ(1.0 + xOffset, 0.0 + zOffset, 1.005 + xOffset, 0.7 + zOffset, 2.0)
  line(1.0 + xOffset, 2.0, 2.1 + xOffset, 2.0, 0.7 + zOffset)

  # GRANDE AREA - AZUL
  lineXtoZ(2.4 + xOffset, 0.0 + zOffset, 2.405 + xOffset, 1.3 + zOffset, 2.0)
  lineXtoZ(0.7 + xOffset, 0.0 + zOffset, 0.705 + xOffset, 1.3 + zOffset, 2.0)
  line(0.7 + xOffset, 2.0, 2.4 + xOffset, 2.0, 1.3 + zOffset)

  # PEQUENA AREA - VERMELHO
  lineXtoZ(2.1 + xOffset, 9.3 + zOffset, 2.105 + xOffset, 10 + zOffset, 2.0)
  lineXtoZ(1.0 + xOffset, 9.3 + zOffset, 1.005 + xOffset, 10 + zOffset, 2.0)
  line(1.0 + xOffset, 2.0, 2.1 + xOffset, 2.0, 9.3 + zOffset)

  # GRANDE AREA - VERMELHO
  lineXtoZ(2.4 + xOffset, 8.7 + zOffset, 2.405 + xOffset, 10 + zOffset, 2.0)
  lineXtoZ(0.7 + xOffset, 8.7 + zOffset, 0.705 + xOffset, 10 + zOffset, 2.0)
  line(0.7 + xOffset, 2.0, 2.4 + xOffset, 2.0, 8.7 + zOffset)
