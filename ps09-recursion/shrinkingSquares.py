# Your name: Anika Shields
# Your username: ashields
# CS111 Spring 2018 PS09
# shrinkingSquares.py
# Submission date: 4/24/18

from cs1graphics import *
from printNice import printNice

#------------------------------------------------------------------------------
# Subtask 3a 

def rotated(vals):
    """
    Suppose vals is a list of values with n elements. 
    Return a **new** list of n elements that contains the same values as vals
    except that the 0th value appears at the end and the index of every other 
    value is shifted down by 1, 
       
    The given list vals is **not** changed by this operation.
    """
    return vals[1:] + vals[0:1]
#-------------------------------------------------------------------------------
# Helper function

def drawSquare(canvas, size, upperLeftX, upperLeftY, color): 
    """
    On the given canvas, add a square of the given size and color whose 
    upper left corner is at (upperLeftX, upperLeftY) in the canvas.
    """
    halfSize = size/2.0
    centerX = upperLeftX + halfSize
    centerY = upperLeftY + halfSize
    sq = Square(size, Point(centerX, centerY))
    sq.setFillColor(color)
    canvas.add(sq)

#------------------------------------------------------------------------------
# Subtask 3b

def drawShrinkingSquaresRow(canvas, size, upperLeftX, upperLeftY, shrinkFactor, 
                            minSize, colorList):
    """
    On the given canvas, add a row of colored squares aligned on their upper
    edges.

    Each square but the first has a left edge that coincides with the right
    edge of the square to its left.

    The leftmost square has an upper left corner at at (upperLeftX,
    upperLeftY) in the canvas.

    The leftmost square has side length `size`, and each other square has a
    side length that is shrinkFactor multiplied by the side length of the
    square immediately to its left. (Assume 0 < `shrinkFactor` < 1.)

    The smallest allowable square has side length `minSize`; no square whose
    side is less than `minSize` will be drawn.

    From left to right, the squares are colored using the colors in order from
    the list of colors `colorList`. When colors run out, they start again at
    the beginning of `colorList`.
    """
    
    if size >= minSize:
        #drawing leftmost square
        drawSquare(canvas, size, upperLeftX, upperLeftY, colorList[0])
    
        #recursive call for square row
        drawShrinkingSquaresRow(canvas, size*shrinkFactor, upperLeftX+size, 
                        upperLeftY, shrinkFactor, minSize, rotated(colorList))


#------------------------------------------------------------------------------
# Subtask 3b
def drawShrinkingSquares(canvas, size, upperLeftX, upperLeftY, shrinkFactor, 
                         minSize, colorList):
    """
    On the given canvas, add rows of colored squares, where each row is
    created by calls to `drawShrinkingSquaresRow` that use the parameters
    `shrinkFactor` and `minSize` unchanged from `drawShrinkingSquaresRow`.

    The top left corner of the uppermost row is at coordinates (upperLeftX,
    upperLeftY) in the canvas.

    The rows are aligned on their leftmost edges, and the top edge of each row
    (but the first) coincides with the bottom edge of the largest square in
    the row above it.
 
    The topmost row is the created by `shrinkingSquaresRow(size, shrinkFactor,
    minSize, colorList)`. Going downward, each row has a leftmost square whose
    side length is `shrinkFactor` multiplied by the side length of the
    leftmost square immediately above it. Smaller rows are added until the
    size of the biggest square in a row would be strictly less than `minSize`.

    The color list used in a row is a version of the list from the row
    immediately above in which the first color has been move to the end but
    all other colors are the same.
    """
    if size >= minSize:
        drawShrinkingSquaresRow(canvas, size, upperLeftX, upperLeftY, 
                                shrinkFactor, minSize, colorList)
        drawShrinkingSquares(canvas, size*shrinkFactor, upperLeftX, 
                    upperLeftY+size, shrinkFactor, minSize, rotated(colorList))

#------------------------------------------------------------------------------
# Testing functions. Do not modify these!

def testRotated(vals): 
    def rotatedNTimes(n):
        result = vals
        for i in range(n):
            result = rotated(result)
        return result
    return [('list rotated {} times: {}'.format(i, rotatedNTimes(i)), 
             'original list is now {}'.format(vals)) 
              for i in range(len(vals)+2)]

def testDrawShrinkingSquaresRow(size, shrinkFactor, minSize, colorList):
    canv = Canvas(800, size, 'white', 
                  'testDrawShrinkingSquaresRow({},{},{},{})'.format(
                     size, shrinkFactor, minSize, colorList))
    drawShrinkingSquaresRow(canv, size, 0, 0, shrinkFactor, 
                            minSize, colorList)

def testDrawShrinkingSquares(size, shrinkFactor, minSize, colorList):
    canv = Canvas(800, 800, 'white', 
                  'testDrawShrinkingSquares({},{},{},{})'.format(
                     size, shrinkFactor, minSize, colorList))
    drawShrinkingSquares(canv, size, 0, 0, shrinkFactor, minSize, colorList)

#------------------------------------------------------------------------------
# Testing cases. Uncomment lines below

if __name__=="__main__":
    '''Testing cases go here'''
    printNice(testRotated(range(4)))
    printNice(testRotated(range(10)))

    testDrawShrinkingSquaresRow(400, 0.5, 5, ['cyan', 'magenta', 'yellow'])
    testDrawShrinkingSquaresRow(300, 0.6, 5, 
      ['yellow', 'green', 'magenta', 'cyan', 'purple'])
    testDrawShrinkingSquaresRow(300, 0.6, 5, ['pink'])
    testDrawShrinkingSquaresRow(200, 0.75, 5, ['red', 'green', 'blue', 
      'magenta', 'cyan', 'yellow', 'orange', 'purple'])
    testDrawShrinkingSquares(400, 0.5, 5, ['cyan', 'magenta', 'yellow'])
    testDrawShrinkingSquares(300, 0.6, 5, 
      ['yellow', 'green', 'magenta', 'cyan', 'purple'])
    testDrawShrinkingSquares(300, 0.6, 5, ['pink'])
    testDrawShrinkingSquares(200, 0.75, 5, ['red', 'green', 'blue', 
      'magenta', 'cyan', 'yellow', 'orange', 'purple'])

