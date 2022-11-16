from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from bresenham import *

def drawGroundLines():
  # lineX, lineY, lineZ = 0.0, 1, 0.0
  xOffset = 0.1
  zOffset = 0.1

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
