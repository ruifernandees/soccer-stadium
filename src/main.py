from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from goalpost import GoalPost
import pygame
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

blueTeamCounter = 0
redTeamCounter = 0

fovY = 75.0
# cameraX, cameraY, cameraZ = 2.0, 3.7, -10.0
cameraX, cameraY, cameraZ = 2.0, 3.7, 7.0
wallX, wallY, wallZ = 0.0, 1.5, 0.0
maxCameraX, maxCameraY, maxCameraZ = 48.0, 10000, 12.0
minCameraX, minCameraY, minCameraZ = -48.0, 0.0, 1.0

wallRotationY = 95.0
wallRotationZ = -90.0
wallRotationX = 0
wallWidth, wallHeight, wallDepth = 0.3, 15.0, 8.0

centerX, centerY, centerZ = wallX, wallY, wallZ
initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ = wallX, wallY + 0.5, wallZ
soccerBallX, soccerBallY, soccerBallZ = initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ
updateSoccerBallX, updateSoccerBallY, updateSoccerBallZ = 1,1,1

def resetSoccerBallPosition():
  global soccerBallX 
  global soccerBallY 
  global soccerBallZ 
  soccerBallX, soccerBallY, soccerBallZ = initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ

def init():
  glClearColor(0.0, 0.0, 0.0, 1.0)

def drawTextStatus():
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


def drawGround():
  # glPushMatrix()
  glTranslatef(wallX, wallY, wallZ)
  glRotatef(wallRotationY, 0.0, 1.0, 0.0)
  glRotatef(wallRotationZ, 0.0, 0.0, 1.0)
  glRotatef(wallRotationX, 1.0, 0.0, 0.0)
  glScalef(wallWidth, wallHeight, wallDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(0.0, 0.5, 0.2)
  glutSolidCube(1.0)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  # glPopMatrix()

def drawSoccerBall():
  glPushMatrix()
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  ballColor = [1, 1, 1]
  glColor3f(ballColor[0], ballColor[1], ballColor[2])
  glTranslatef(soccerBallX, soccerBallY, soccerBallZ)
  glutSolidSphere(0.1, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glPopMatrix()


def drawSky():
  # glPushMatrix()
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  skyBlue = [0.53, 0.81, 0.92]
  glColor3f(skyBlue[0], skyBlue[1], skyBlue[2])
  glTranslatef(0, 0, 0 )
  glutSolidSphere(50, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  # glPopMatrix()


def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glEnable(GL_DEPTH_TEST)
  glMatrixMode(GL_MODELVIEW) 
  glLoadIdentity()

  gluLookAt(cameraX, cameraY, cameraZ, centerX, centerY, centerZ, 0.0, 1.0, 0.0)
  drawTextStatus()
  drawSoccerBall()
  gp1 = GoalPost('blue')
  gp1.draw()
  gp2 = GoalPost('red')
  gp2.draw()
  drawGround() 
  drawSky()

  glutSwapBuffers()


def idleDisplay():
  glutPostRedisplay()

def reshape(w, h):
  pass

def keyCallback(key, x, y):
  global cameraZ 
  global soccerBallX 
  global soccerBallY 
  global soccerBallZ 
  global blueTeamCounter 
  global redTeamCounter 
  offset = 0.2
  if (key == b'a'):
    soccerBallX -= offset
    # print("Hello Key A", soccerBallX)
  if (key == b'd'):
    soccerBallX += offset
    # print("Hello Key D", soccerBallX)
  if (key == b'w'):
    soccerBallZ -= offset
    # print("Hello Key W", soccerBallZ)
  if (key == b's'):
    soccerBallZ += offset
    # print("Hello Key S", soccerBallZ)
  if (key == b'e'):
    # print("Hello Key E")
    cameraZ -= offset
  if (key == b'q'):
    cameraZ += offset
    # print("Hello Key Q")

  blueTeamGoal = -6.4
  redTeamGoal = 6.4

  if (soccerBallZ <= blueTeamGoal):
    blueTeamCounter += 1
    gameStatus()
    resetSoccerBallPosition()
  elif (soccerBallZ >= redTeamGoal):
    redTeamCounter += 1
    gameStatus()
    resetSoccerBallPosition()
    
  glutPostRedisplay()

def configureLight():
	light_ambient = [0.2, 0.2, 0.2]
	light_position = [cameraX, cameraY, cameraZ, 0.0]
	
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

def gameStatus():
  print("PLACAR: ")
  print("AZUL: ", blueTeamCounter)
  print("VERMELHO: ", redTeamCounter)


def main():
  print('PID: ',os.getpid())
  glutInit()
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowPosition(0,500)
  glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
  glutCreateWindow("Campo de Futebol - CG")
  init()
  glutDisplayFunc(display)
  glutIdleFunc(idleDisplay)
  glutReshapeFunc(reshape)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(fovY, 1.0 * WINDOW_WIDTH / WINDOW_HEIGHT, 0.001, 1000.0)
  glutKeyboardFunc(keyCallback)
  configureLight()
  gameStatus()
  glutMainLoop()
  

if __name__ == "__main__":
    main()