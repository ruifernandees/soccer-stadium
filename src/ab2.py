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
wallX, wallY, wallZ = 0.0, 1, 0.0
maxCameraX, maxCameraY, maxCameraZ = 48.0, 10000, 12.0
minCameraX, minCameraY, minCameraZ = -48.0, 0.0, 1.0

wallRotationY = 95.0
wallRotationZ = -90.0
wallRotationX = 0
wallWidth, wallHeight, wallDepth = 1, 15.0, 8.0

centerX, centerY, centerZ = wallX, wallY, wallZ
initialSoccerBallX, initialSoccerBallY, initialSoccerBallZ = wallX, wallY + 0.8, wallZ
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
    print(x,y)
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

# def lineZ(z1, z2, x, y):
#   # a = (z2-z1)/(x2-x1)
#   a = 0
#   z = z1
#   while z <= z2:
#     # x+=0.0005
#     z += bresenhamOffset
#     x = (0 + a * (z - z1))
#     glBegin(GL_POINTS)
#     glColor3f(1,1,1)
#     glVertex3f(x,y,z)
#     glEnd()

def init():
  glClearColor(0.0, 0.0, 0.0, 1.0)

def drawGround():
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

def drawGroundLines():
  lineX, lineY, lineZ = 0.0, 1, 0.0
  line(0.0, 2.0, 3.0, 2.0, 0.0)
  lineXtoZ(3.0, 0.0, 3.1, 10.0, 2.0)
  lineXtoZ(0.0, 0.0, 0.1, 10.0, 2.0)
  line(0.1, 2.0, 3.1, 2.0, 10.0)
  

def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glEnable(GL_DEPTH_TEST)
  glMatrixMode(GL_MODELVIEW) 
  glLoadIdentity()

  gluLookAt(cameraX, cameraY, cameraZ, centerX, centerY, centerZ, 0.0, 1.0, 0.0)
  drawGroundLines()

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
  global soccerBallRotationX 
  global soccerBallRotationY 
  global soccerBallRotationZ 
  global blueTeamCounter 
  global redTeamCounter 
  offset = 0.2
  rotationOffset = 20
  if (key == b'a'):
    soccerBallX -= offset
    soccerBallRotationZ -= rotationOffset
    # print("Hello Key A", soccerBallX)
  if (key == b'd'):
    soccerBallX += offset
    soccerBallRotationZ += rotationOffset
    # print("Hello Key D", soccerBallX)
  if (key == b'w'):
    soccerBallZ -= offset
    soccerBallRotationX -= rotationOffset
    # print("Hello Key W", soccerBallZ)
  if (key == b's'):
    soccerBallZ += offset
    soccerBallRotationX += rotationOffset
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