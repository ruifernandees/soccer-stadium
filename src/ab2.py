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
cameraX, cameraY, cameraZ = 2.0, 3.7, 7.0
wallX, wallY, wallZ = 0.0, 2.0, 0.0
maxCameraX, maxCameraY, maxCameraZ = 48.0, 10000, 12.0
minCameraX, minCameraY, minCameraZ = -48.0, 0.0, 1.0

wallRotationY = 95.0
wallRotationZ = -90.0
wallRotationX = 0
wallWidth, wallHeight, wallDepth = 4.5, 2.0, 10.5

centerX, centerY, centerZ = wallX, wallY, wallZ
initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ = 1.6, 2.1, 5.20
soccerBallRotationX, soccerBallRotationY, soccerBallRotationZ = 0,0,0
soccerBallX, soccerBallY, soccerBallZ = initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ
updateSoccerBallX, updateSoccerBallY, updateSoccerBallZ = 1,1,1

bresenhamOffset = 0.005

def line(x1, y1, x2, y2, z):
  a = (y2-y1)/(x2-x1)
  x = x1
  while x <= x2:
    x+=bresenhamOffset
    y = (y1 + a * (x - x1))
    # print(x,y)
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(x,y,z)
    glEnd()

def lineXtoZ(x1, z1, x2, z2, y):
  a = (z2-z1)/(x2-x1)
  x = x1
  while x <= x2:
    x+=0.00005
    z = (z1 + a * (x - x1))
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(x,y,z)
    glEnd()

def init():
  glClearColor(0.0, 0.0, 0.0, 1.0)

def drawGround():
  glTranslatef(wallWidth/3, wallHeight/2 , (wallDepth/2) )
  glScalef(wallWidth, wallHeight, wallDepth)

  glEnable(GL_COLOR_MATERIAL)
  glColor3f(0.0, 0.5, 0.2)
  glutSolidCube(1.0)

  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

def drawSky():
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  skyBlue = [0.53, 0.81, 0.92]
  glColor3f(skyBlue[0], skyBlue[1], skyBlue[2])
  glTranslatef(0, 0, 0)
  glutSolidSphere(50, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


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


def drawSoccerBall():
  glPushMatrix()
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  ballColor = [1, 1, 1]
  glColor3f(ballColor[0], ballColor[1], ballColor[2])
  glTranslatef(soccerBallX, soccerBallY, soccerBallZ)
  glRotatef(soccerBallRotationY, 0.0, 1.0, 0.0)
  glRotatef(soccerBallRotationZ, 0.0, 0.0, 1.0)
  glRotatef(soccerBallRotationX, 1.0, 0.0, 0.0)
  glutWireSphere(0.015, SLICES, STACKS)
  glutSolidSphere(0.015, SLICES, STACKS)
  glColor3f(0, 0, 0)
  # glutSolidCube(0.035)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glPopMatrix()

def resetSoccerBallPosition():
  global soccerBallX 
  global soccerBallY 
  global soccerBallZ 
  soccerBallX, soccerBallY, soccerBallZ = initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ
 

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
  drawGroundLines()
  drawGround()
  drawSky()

  glutSwapBuffers()


def idleDisplay():
  glutPostRedisplay()

def reshape(w, h):
  pass

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


def gameStatus():
  print("PLACAR: ")
  print("AZUL: ", blueTeamCounter)
  print("VERMELHO: ", redTeamCounter)


def configureLight():
	light_ambient = [0.7, 0.7, 0.7]
	light_position = [cameraX, cameraY, cameraZ, 0.0]
	
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

def keyCallback(key, x, y):
  global cameraZ 
  global soccerBallX 
  global soccerBallY 
  global soccerBallZ 
  global soccerBallRotationX 
  global soccerBallRotationY 
  global soccerBallRotationZ 
  global blueTeamCounter 
  global redTeamCounter 
  offset = 0.1
  rotationOffset = 20
  if (key == b'a'):
    soccerBallX -= offset
    soccerBallRotationZ -= rotationOffset
  if (key == b'd'):
    soccerBallX += offset
    soccerBallRotationZ += rotationOffset
  if (key == b'w'):
    soccerBallZ -= offset
    soccerBallRotationX -= rotationOffset
  if (key == b's'):
    soccerBallZ += offset
    soccerBallRotationX += rotationOffset
  if (key == b'e'):
    cameraZ -= offset
  if (key == b'q'):
    cameraZ += offset
  print(soccerBallX, soccerBallY, soccerBallZ)

  blueTeamGoal = 0.20000000000000193
  redTeamGoal = 10.2

  if (soccerBallZ <= blueTeamGoal):
    blueTeamCounter += 1
    gameStatus()
    resetSoccerBallPosition()
  elif (soccerBallZ >= redTeamGoal):
    redTeamCounter += 1
    gameStatus()
    resetSoccerBallPosition()
    
  glutPostRedisplay()


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
  
  glutMainLoop()
  

if __name__ == "__main__":
    main()