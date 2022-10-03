from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

fovY = 75.0
cameraX, cameraY, cameraZ = 1.0, 1.7, 5.0
wallX, wallY, wallZ = 0.0, 1.5, 0.0
maxCameraX, maxCameraY, maxCameraZ = 48.0, 10000, 12.0
minCameraX, minCameraY, minCameraZ = -48.0, 0.0, 1.0

wallRotationY = 95.0
wallRotationZ = -90.0
wallRotationX = 0
wallWidth, wallHeight, wallDepth = 0.3, 20.0, 20.0

centerX, centerY, centerZ = wallX, wallY, wallZ

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

def drawSoccerBall():
  SLICES, STACKS = 15, 15
  glEnable(GL_COLOR_MATERIAL)
  ballColor = [1, 0, 0]
  glColor3f(ballColor[0], ballColor[1], ballColor[2])
  glTranslatef(4.0, 4.0, 4.0)
  glutSolidSphere(0.1, SLICES, STACKS)
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
  glTranslatef(centerX, centerY, centerZ )
  glutSolidSphere(50, SLICES, STACKS)
  mat_specular = [0.0, 0.0, 0.0]
  mat_shininess = [0.0]
  glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
  glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glEnable(GL_DEPTH_TEST)
  glMatrixMode(GL_MODELVIEW) 
  glLoadIdentity()

  gluLookAt(cameraX, cameraY, cameraZ, centerX, centerY, centerZ, 0.0, 1.0, 0.0)

  drawGround()
  drawSky()
  drawSoccerBall()

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
  offset = 1.0
  global minCameraZ
  global maxCameraZ
  if (key == b'a' and minCameraX < centerX):
    centerX -= offset
    print("Hello Key A", centerX)
    # cameraY -= offset
  if (key == b'd' and maxCameraX > centerX):
    centerX += offset
    print("Hello Key D", centerX)
    # cameraY += offset
  if (key == b'w' and minCameraZ < cameraZ):
    cameraZ -= offset
    print("Hello Key W", cameraZ)
  if (key == b's' and maxCameraZ > cameraZ):
    cameraZ += offset
    print("Hello Key S", cameraZ)
  # if (key == b'e'):
  #   print("Hello Key E")
  #   centerX -= offset
  # if (key == b'q'):
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