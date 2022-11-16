from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from goalpost import GoalPost

from drawGroundLines import *
from dayAndNightLight import *
from drawSoccerBall import *
from drawTextStatus import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

blueTeamCounter = 0
redTeamCounter = 0

fovY = 75.0
cameraX, cameraY, cameraZ = 2.0, 3.7, 12.4
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

isDay = True

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
  configureLight()

  gluLookAt(cameraX, cameraY, cameraZ, centerX, centerY, centerZ, 0.0, 1.0, 0.0)
  drawTextStatus(blueTeamCounter, redTeamCounter)
  drawSoccerBall(soccerBallX, soccerBallY, soccerBallZ, soccerBallRotationX, soccerBallRotationY, soccerBallRotationZ)
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



def gameStatus():
  print("PLACAR: ")
  print("AZUL: ", blueTeamCounter)
  print("VERMELHO: ", redTeamCounter)


def configureLight():
  global cameraX 
  global cameraY 
  global cameraZ 
  global isDay
  if (isDay):
    dayLight(cameraX, cameraY, cameraZ)
  else:
    nightLight(cameraX, cameraY, cameraZ)


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
  global isDay
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
  if (key == b'n'):
    isDay = not isDay
  print(soccerBallX, soccerBallY, soccerBallZ)
  print(cameraX, cameraY, cameraZ)

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

  
  glutMainLoop()
  

if __name__ == "__main__":
    main()