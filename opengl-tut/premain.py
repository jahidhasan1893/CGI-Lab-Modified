from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Line.dda import ddaAlgo
from Line.bresenham import bresenham
# import numpy as np

def myInit():
    # glClearColor(1.0, 1.0, 0.0, 1.0)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(0.2, 0.5, 0.4)
    glPointSize(5.0)  # 35, 15, 15 | 10, 50, 50 | 7, 75, 75 | 7,(-10, 75, -10, 75)
    gluOrtho2D(-54, 51, -54, 51)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # y-axis
    glBegin(GL_LINES)
    glVertex2f(0, -54)
    glVertex2f(0, 54)
    glEnd()

    # x-axis
    glBegin(GL_LINES)
    glVertex2f(-54, 0)
    glVertex2f(51, 0)
    glEnd()

    # Center
    # glBegin(GL_POINTS)
    # glVertex2f(0, 0)
    # glEnd()

    # line_pixel = ddaAlgo([5, 3], [10, 10])
    # line_pixel = ddaAlgo([1, 1], [10, 10])
    line_pixel1 = bresenham([0, 0], [10, 10])

    # x1 = float(input('Give x1:'))
    # y1 = float(input('Give y1:'))
    # x2 = float(input('Give x2:'))
    # y2 = float(input('Give y2:'))
    # print(x1, y1, x2, y2)
    # start = [x1,y1]
    # end = [x2,y2]
    # line_pixel = ddaAlgo(start, end)


    glBegin(GL_POINTS)
    for pixel in line_pixel1:
        print(pixel)
        glVertex2f(pixel[0], pixel[1])
    # glVertex2f(300, 200)
    glEnd()

    # glBegin(GL_POINTS)
    # for pixel in line_pixel1:
    #     print(pixel)
    #     glVertex2f(pixel[0], pixel[1])
    # # glVertex2f(300, 200)
    # glEnd()

    # glBegin( GL_QUADS )
    # glVertex2f( 100.0, 100.0 )
    # glVertex2f( 300.0, 100.0 )
    # glVertex2f( 300.0, 200.0 )
    # glVertex2f( 100.0, 200.0 )
    # glEnd()

    # glBegin(  GL_TRIANGLE_STRIP )
    # glVertex2f( 100.0, 210.0 )
    # glVertex2f( 300.0, 210.0 )
    # glVertex2f( 300.0, 310.0 )
    # glEnd()

    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
# glutInitWindowPosition(100, 100)
glutInitWindowPosition(350, 100)
glutCreateWindow("My OpenGL Code")
myInit()
glutDisplayFunc(display)
glutMainLoop()