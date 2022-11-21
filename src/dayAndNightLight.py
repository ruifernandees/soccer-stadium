from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def dayLight(cameraX, cameraY, cameraZ):
	light_ambient = [0.7, 0.7, 0.7]
	light_position = [0.0, 10.0, 0.0, 0.0]
	
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)

def nightLight(cameraX, cameraY, cameraZ):
	light_ambient = [0.4, 0.4, 0.4]
	
	# glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	# glLightfv(GL_LIGHT0, GL_POSITION, [-5.1, 4.5 , -5.0, 0.0])
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)