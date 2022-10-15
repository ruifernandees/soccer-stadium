from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

fovY = 75.0
cameraX, cameraY, cameraZ = 2.0, 2.7, 5.0
wallX, wallY, wallZ = 0.0, 1.5, 0.0
maxCameraX, maxCameraY, maxCameraZ = 48.0, 10000, 12.0
minCameraX, minCameraY, minCameraZ = -48.0, 0.0, 1.0

wallRotationY = 95.0
wallRotationZ = -90.0
wallRotationX = 0
wallWidth, wallHeight, wallDepth = 0.3, 5.0, 5.0

centerX, centerY, centerZ = wallX, wallY, wallZ
soccerBallX, soccerBallY, soccerBallZ = wallX, wallY + 0.5, wallZ
updateSoccerBallX, updateSoccerBallY, updateSoccerBallZ = 1,1,1

def init():
  glClearColor(0.0, 0.0, 0.0, 1.0)

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
  # glTranslatef(updateSoccerBallX * (centerX+0.5), updateSoccerBallY * (centerY+0.5), updateSoccerBallZ * centerZ)
  glTranslatef( (soccerBallX),  (soccerBallY),  soccerBallZ)
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

  drawSoccerBall()
  drawGround() 
  drawSky()

  glutSwapBuffers()


def idleDisplay():
  glutPostRedisplay()

def reshape(w, h):
  pass

def keyCallback(key, x, y):
  global cameraY 
  global cameraZ 
  global cameraX 
  global centerX 
  global centerY 
  global centerZ 
  global soccerBallX 
  global soccerBallY 
  global soccerBallZ 
  offset = 0.2
  global minCameraZ
  global maxCameraZ
  if (key == b'a' and minCameraX < soccerBallX):
    soccerBallX -= offset
    print("Hello Key A", soccerBallX)
  if (key == b'd' and maxCameraX > soccerBallX):
    soccerBallX += offset
    print("Hello Key D", soccerBallX)
  if (key == b'w' and minCameraZ < cameraZ):
    soccerBallZ -= offset
    print("Hello Key W", cameraZ)
  if (key == b's' and maxCameraZ > cameraZ):
    soccerBallZ += offset
    print("Hello Key S", cameraZ)
  # if (key == b'e'):
  #   print("Hello Key E")
  #   cameraZ -= offset
  # if (key == b'q'):
  #   cameraZ += offset
  #   print("Hello Key Q")
    
  glutPostRedisplay()

def configureLight():
	light_ambient = [0.2, 0.2, 0.2]
	light_position = [cameraX, cameraY, cameraZ, 0.0]
	
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)


def main():
  print('PID: ',os.getpid())
  glutInit()
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowPosition(0,500)
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