from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

goalPostX, goalPostY, goalPostZ = 0.0, 1.5, 0.0

goalPostRotationY = 95.0
goalPostRotationZ = -90.0
goalPostRotationX = 0

goalPostDepthFirst = 0.1
goalPostDepthSecond = 10.1
blueTeamColor = [0,0,1]
redTeamColor = [1,0,0]

class GoalPost:
  def __init__(self, mode):
    self.mode = mode 

  def draw(self):
    self.drawGoalPostVerticalLeft()
    self.drawGoalPostVerticalRight()
    self.drawGoalPostHorizontal()

  def drawGoalPostVerticalLeft(self):
    glPushMatrix()
    # TOCO 1
    goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth = 1.67, 0.03, 0.03
    if (self.mode == 'blue'):
      goalPostX, goalPostY, goalPostZ = 1.3, 1.5, goalPostDepthFirst
    elif (self.mode == 'red'):
      goalPostX, goalPostY, goalPostZ = 1.3, 1.5, goalPostDepthSecond
    glTranslatef(goalPostX, goalPostY, goalPostZ)
    glRotatef(10.0, 0.0, 1.0, 0.0)
    glRotatef(goalPostRotationZ, 0.0, 0.0, 1.0)
    glRotatef(goalPostRotationX, 1.0, 0.0, 0.0)
    glScalef(goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth)

    glEnable(GL_COLOR_MATERIAL)
    if (self.mode == 'blue'):
      glColor3f(blueTeamColor[0], blueTeamColor[1], blueTeamColor[2])
    elif (self.mode == 'red'):
      glColor3f(redTeamColor[0], redTeamColor[1], redTeamColor[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glPopMatrix()

  def drawGoalPostVerticalRight(self):
    glPushMatrix()
    # TOCO 2
    goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth = 1.65, 0.03, 0.03
    if (self.mode == 'blue'):
      goalPostX, goalPostY, goalPostZ = 2, 1.5, goalPostDepthFirst
    elif (self.mode == 'red'):
      goalPostX, goalPostY, goalPostZ = 2, 1.5,goalPostDepthSecond
    glTranslatef(goalPostX, goalPostY, goalPostZ)
    glRotatef(10.0, 0.0, 1.0, 0.0)
    glRotatef(goalPostRotationZ, 0.0, 0.0, 1.0)
    glRotatef(goalPostRotationX, 1.0, 0.0, 0.0)
    glScalef(goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth)

    glEnable(GL_COLOR_MATERIAL)
    if (self.mode == 'blue'):
      glColor3f(blueTeamColor[0], blueTeamColor[1], blueTeamColor[2])
    elif (self.mode == 'red'):
      glColor3f(redTeamColor[0], redTeamColor[1], redTeamColor[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glPopMatrix()

  def drawGoalPostHorizontal(self):
    glPushMatrix()
    goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth = 0.03, 0.7, 0.03
    if (self.mode == 'blue'):
      goalPostX, goalPostY, goalPostZ = 1.66, 2.32, goalPostDepthFirst
      goalPostRotationY = 10.0
      goalPostRotationZ = -90.0
      goalPostRotationX = 10
    elif (self.mode == 'red'):
      goalPostX, goalPostY, goalPostZ = 1.66, 2.32,goalPostDepthSecond
      goalPostRotationY = 10.0
      goalPostRotationZ = -90.0
      goalPostRotationX = 10
    glTranslatef(goalPostX, goalPostY, goalPostZ)
    glRotatef(goalPostRotationY, 0.0, 1.0, 0.0)
    glRotatef(goalPostRotationZ, 0.0, 0.0, 1.0)
    glRotatef(goalPostRotationX, 1.0, 0.0, 0.0)
    glScalef(goalPostVerticalWidth, goalPostVerticalHeight, goalPostVerticalDepth)

    glEnable(GL_COLOR_MATERIAL)
    if (self.mode == 'blue'):
      glColor3f(blueTeamColor[0], blueTeamColor[1], blueTeamColor[2])
    elif (self.mode == 'red'):
      glColor3f(redTeamColor[0], redTeamColor[1], redTeamColor[2])
    glutSolidCube(1.0)

    mat_specular = [0.0, 0.0, 0.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glPopMatrix()