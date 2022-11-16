from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *

def drawTextStatus(blueTeamCounter, redTeamCounter):
  blueTeamText = f'TIME AZUL: {blueTeamCounter}'

  redTeamText = f'TIME VERMELHO: {redTeamCounter}'

  pygame.font.init()
  font = pygame.font.SysFont('arial', 32)

  x, y = 0, 32
  textSurface = font.render(blueTeamText, True, (255, 255, 66, 255), (0, 66, 0, 255))
  textData = pygame.image.tostring(textSurface, "RGBA", True)
  glWindowPos2d(x, y)
  glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

  x, y = 0, 0 
  textSurface = font.render(redTeamText, True, (255, 255, 66, 255), (0, 66, 0, 255))
  textData = pygame.image.tostring(textSurface, "RGBA", True)
  glWindowPos2d(x, y)
  glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
