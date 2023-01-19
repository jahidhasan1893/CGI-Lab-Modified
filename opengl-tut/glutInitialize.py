from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

figures = []


def myInit():
    # Set background color
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(0.2, 0.5, 0.4)
    glPointSize(5.0)  # 35, 15, 15 | 10, 50, 50 | 7, 75, 75 | 7,(-10, 75, -10, 75)
    gluOrtho2D(-54, 51, -54, 51)


def displayPoints():
    glClear(GL_COLOR_BUFFER_BIT)

    # x-axis
    glBegin(GL_LINES)
    glVertex2f(-54, 0)
    glVertex2f(51, 0)
    glEnd()

    # y-axis
    glBegin(GL_LINES)
    glVertex2f(0, -54)
    glVertex2f(0, 54)
    glEnd()

    # Center
    # glBegin(GL_POINTS)
    # glVertex2f(0, 0)
    # glEnd()

    # Rectangle
    # glBegin( GL_QUADS )
    # glVertex2f( 100.0, 100.0 )
    # glVertex2f( 300.0, 100.0 )
    # glVertex2f( 300.0, 200.0 )
    # glVertex2f( 100.0, 200.0 )
    # glEnd()

    # Triangle
    # glBegin(  GL_TRIANGLE_STRIP )
    # glVertex2f( 100.0, 210.0 )
    # glVertex2f( 300.0, 210.0 )
    # glVertex2f( 300.0, 310.0 )
    # glEnd()

    for pixels in figures:
        for pixel in pixels:
            # Draw a pixel(x,y)
            if len(pixel) == 2:
                glBegin(GL_POINTS)
                glVertex2f(pixel[0], pixel[1])
                glEnd()
            else:
                # Logic for striped line(x1, y1, x2, y2, isStriped)
                if len(pixel) == 5:
                    glLineStipple(1, 0xAAAA)
                    glEnable(GL_LINE_STIPPLE)
                else:
                    glDisable(GL_LINE_STIPPLE)

                # Draw a line P1(x1,y1) & P2(x2,y2)
                glBegin(GL_LINES)
                glVertex2f(pixel[0], pixel[1])
                glVertex2f(pixel[2], pixel[3])
                glEnd()
    glFlush()


def gluteSetup(figure):
    global figures
    figures = figure
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 100)
    glutCreateWindow("My OpenGL Code")
    myInit()
    glutDisplayFunc(displayPoints)
    glutMainLoop()
