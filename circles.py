# Your name: Anika Shields
# Your username: ashields
# CS111 PS05 Task 1
# circles.py
# Submission date: 3/9/18

from cs1graphics import *

def concentricCircles(size, numCircles, colorList):
    """Creates and *returns* a Layer containing numCircles
       circles, all of which are centered at (0, 0).
       Let r be the radius of the smallest circle. Then the radii of
       the circles grow in arithmetic progression -- r, 2r, 3r, etc. --
       up to the radius of the largest circle, which is size/2.
       The smallest circle is filled with color1 and afterwards the colors are
       alternated between color1 and color2.
    """

    concentricCircles = Layer()
    r = size/2.0 

    for i in range(numCircles,0,-1):
        circle1 = Circle(r,Point(0,0))
        circle1.setFillColor(colorList[(i+1)%len(colorList)])
        circle1.scale((1.0/numCircles*(i+0)))
        concentricCircles.add(circle1)
    return concentricCircles
        

def showConcentricCircles(canvasSize, numCircles, colorList):
    """Creates and *returns* a canvasSize x canvasSize white canvas containing
       numCircles concentric circles, with the smallest circle having color1
       and alternating with color2. The title of the canvas should
       be a string representation of the invocation of the showConcentricCircles
       function that created the canvas.
    """
    canvas = Canvas(canvasSize,canvasSize,'white','showConcentricCircles('+ 
            str(canvasSize) + ', ' + str(numCircles) + ', ' + 
            str(colorList)+')')
    circs = concentricCircles(canvasSize, numCircles, colorList)
    circs.moveTo((canvasSize/2),(canvasSize/2))
    canvas.add(circs)
    return canvas
    
def circleRow(numCirclesInRow, size, numCircles, colorList):
    """Creates and *returns* a numCirclesInRow*size x size white canvas containing
       numCirclesInRow circles, each of which is a concentric circle (created
       by invoking concentricCircles). The distance between the center of each
       successive circle is size. The title of the canvas should be a string
       representation of the invocation of the circleRow function that
       created the canvas.
    """
    canvas1 = Canvas((numCirclesInRow*size),size,'white','circleRow('+ 
            str(numCirclesInRow) + ', ' + str(size) + ', ' + str(numCircles) + 
            ', ' + str(colorList)+')')
    
    for i in range(numCirclesInRow):
        circs = concentricCircles(size, numCircles, colorList)
        circs.moveTo((size/2.),(size/2.))
        circs.move(i*size,0)
        canvas1.add(circs)
    return canvas1
    
    
if __name__ == "__main__":
  '''All code that tests Task 2 functions should be nested
     within this special "main" conditional.
  '''
  # # Subtask 1a
  # paper1 = Canvas(200, 200)
  # cybla = concentricCircles(200, 5, ['cyan', 'red'])
  # paper1.add(cybla)
  # cybla.move(100, 100)

# Subtask 1b
# cybla = showConcentricCircles(200, 5, ['cyan', 'black'])
# grellow = showConcentricCircles(400, 8, ['green', 'yellow'])
# reblu = showConcentricCircles(500, 13, ['red', 'blue'])
# pima = showConcentricCircles(500, 2, ['pink', 'magenta'])

#Subtask 1c
single = circleRow(1,500,7,['orange','yellow'])
triple = circleRow(3,400,10,['red','pink'])
quint = circleRow(5,240,8,['blue','green'])
dozen = circleRow(12,100,10,['black','white'])
