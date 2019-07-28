# Fall 2017 PS02
# Sohie Lee 
# bunny.py
# Provides bunny pattern for PS02 Tasks 2 and 3

from cs1graphics import *
from cs1graphicsHelper import *
from graphicsState import *

bunny = Layer()

leftEar = Ellipse(40,100,Point(-25,-55))
leftEar.setFillColor('white')
leftEar.rotate(-10)
bunny.add(leftEar)

rightEar = Ellipse(40,100,Point(25,-55))
rightEar.setFillColor('white')
rightEar.rotate(10)
bunny.add(rightEar)

leftInnerEar = Ellipse(20,80, Point(-25,-55))
leftInnerEar.setFillColor('pink')
leftInnerEar.rotate(-10)
bunny.add(leftInnerEar)

rightInnerEar = Ellipse(20,80, Point(25,-55))
rightInnerEar.setFillColor('pink')
rightInnerEar.rotate(10)
bunny.add(rightInnerEar)

face = Ellipse(105, 95, Point(0,25))
face.setFillColor('white')
bunny.add(face)

nose = Polygon(Point(2,51), Point(-2,51), Point(-10,41), Point(-9, 40), Point(8,40), Point(10, 42))
nose.setBorderColor('grey')
nose.setFillColor('grey')
bunny.add(nose)

leftEye = Circle(7, Point(-20,15))
leftEye.setFillColor('lightblue')
leftEye.setBorderColor('lightblue')
rightEye = Circle(7, Point(20, 15))
rightEye.setFillColor('lightblue')
rightEye.setBorderColor('lightblue')
bunny.add(leftEye)
bunny.add(rightEye)

# done with bunny now

# add bunny to canvas and position so fully visible
# paper = Canvas(500,500, 'white','yummy')
# paper.add(bunny)
# bunny.moveTo(250,250)
# drawReferencePoints(paper)  # yields good image for pset, indicating reference point of bunny


# unused code below
# make bunny rotation tile
#tile = Layer()
#bunnyA = bunny.clone()
#bunnyB = bunny.clone()
#bunnyC = bunny.clone()
#bunnyD = bunny.clone()
## put 4 bunnies, each rotated 90 degrees, and make wall-paper style background
## center point of each bunny is center of face
#tile.add(bunnyA)
#bunnyA.move(100,125)
#bunnyB.move(300,125)
#tile.add(bunnyB)
#bunnyB.rotate(180)
#tile.add(bunnyC)
#bunnyC.move(100,375)
#bunnyC.rotate(180)
#tile.add(bunnyD)
#bunnyD.move(300,375)

# paper.add(tile) == 2x2 grid of bunnies, cute

#tileRow = Layer()
#tile1 = tile.clone()
#tileRow.add(tile1)
#tile2 = tile.clone()
#tileRow.add(tile2)
#tile2.move(250,0)
#
#paper.add(tile)


