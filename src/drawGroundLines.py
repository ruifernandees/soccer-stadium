from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from bresenham import *
from bresenhamCircle import *


def drawGroundLines():
  # lineX, lineY, lineZ = 0.0, 1, 0.0
  xOffset = 0.1
  zOffset = 0.6

  # MINI CIRCLE - BLUE TEAM
  goalpost_mini_circle_x, goalpost_mini_circle_y, goalpost_mini_circle_z, goalpost_mini_circle_r = 1.5 + xOffset, 2.036, 1.1 + zOffset, 0.009
  BresenhamCircleDrawXZ(goalpost_mini_circle_x, goalpost_mini_circle_z, goalpost_mini_circle_r, goalpost_mini_circle_y)

  # MINI CIRCLE - RED TEAM
  goalpost_mini_circle_x, goalpost_mini_circle_y, goalpost_mini_circle_z, goalpost_mini_circle_r = 1.55 + xOffset, 2.036, 9.1 + zOffset, 0.009
  BresenhamCircleDrawXZ(goalpost_mini_circle_x, goalpost_mini_circle_z, goalpost_mini_circle_r, goalpost_mini_circle_y)

  central_circle_x, central_circle_y, central_circle_z, central_circle_r = 1.5 + xOffset, 2.0, 5.0 + zOffset, 0.02
  BresenhamCircleDrawXZ(central_circle_x, central_circle_z, central_circle_r, central_circle_y)
  central_circle_x, central_circle_y, central_circle_z, central_circle_r = 1.5 + xOffset, 2.0, 5.0 + zOffset, 0.009
  BresenhamCircleDrawXZ(central_circle_x, central_circle_z, central_circle_r, central_circle_y)

  central_circle_x, central_circle_y, central_circle_z, central_circle_r = 1.5 + xOffset, 2.0, 5.0 + zOffset, 0.5
  BresenhamCircleDrawXZ(central_circle_x, central_circle_z, central_circle_r, central_circle_y)

  half_moon_blue_x, half_moon_blue_y, half_moon_blue_z, half_moon_blue_r = 1.5 + xOffset, 2.0, 1.3 + zOffset, 0.5
  BresenhamCircleDrawXZ(half_moon_blue_x, half_moon_blue_z, half_moon_blue_r, half_moon_blue_y)

  half_moon_red_x, half_moon_red_y, half_moon_red_z, half_moon_red_r = 1.6 + xOffset, 2.0, 8.7 + zOffset, 0.5
  BresenhamCircleDrawXZ(half_moon_red_x, half_moon_red_z, half_moon_red_r, half_moon_red_y)

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

  # ESCANTEIO 1 - AZUL
  escanteio_x, escanteio_y, escanteio_z, escanteio_r = 0.065 + xOffset, 2.0, 0.065 + zOffset, 0.07
  BresenhamCircleDrawXZ(escanteio_x, escanteio_z, escanteio_r, escanteio_y)

  # ESCANTEIO 2 - AZUL
  escanteio_x, escanteio_y, escanteio_z, escanteio_r = 2.94 + xOffset, 2.0, 0.055 + zOffset, 0.07
  BresenhamCircleDrawXZ(escanteio_x, escanteio_z, escanteio_r, escanteio_y)

  # ESCANTEIO 1 - VERMELHO 
  escanteio_x, escanteio_y, escanteio_z, escanteio_r = 0.163 + xOffset, 2.0, 9.943 + zOffset, 0.07
  BresenhamCircleDrawXZ(escanteio_x, escanteio_z, escanteio_r, escanteio_y)

  # ESCANTEIO 2 - VERMELHO 
  escanteio_x, escanteio_y, escanteio_z, escanteio_r = 3.037 + xOffset, 2.0, 9.939 + zOffset, 0.07
  BresenhamCircleDrawXZ(escanteio_x, escanteio_z, escanteio_r, escanteio_y)

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
