# Your name: Anika Shields
# Your username: ashields
# CS111 PS02 Task 1
# debugGraphicsFixed.py
# Submission date: 02/13/18

###############################################################################
# CS111 PS02 Task 1
# 
# Initially, this file contains the buggy contents of Lois Reasoner's 
# debugGraphics.py file. 
# 
# Your task is to modify this file by finding and fixing as many bugs 
# bugs as you can find. 
# 
# You should summarize all bugs and their fixes by assigning variables
# named bug1, fix1, bug2, fix2 at the end of this file, as explained 
# in the Task 1 description. 
#
###############################################################################

from cs1graphics import * 
from graphicsState import * # Useful for debugging. See Lec 03 Notebook
from cs1graphicsHelper import * # Useful for debugging. See Lec 03 Notebook


# Create the "world" that holds the faces
world = Canvas(800, 600, 'paleturquoise', 'Faces')

# A face = a Layer that will have a head, eyes/browse, nose, and mouth
# The reference point of the face is at its center.
face = Layer()
world.add(face)

# The head is the rectangular base for holding eyes/browe, nose, and mouth 
head = Rectangle(200,160)
face.add(head)
head.setFillColor('palegreen')

# rightEyeAndBrow combines right eye and brow into a single cloneable unit
rightEyeAndBrow = Layer()
face.add(rightEyeAndBrow)

# eye of right eye/brow unit 
eye = Ellipse(15,30,Point(50,0))
rightEyeAndBrow.add(eye)
eye.setFillColor('white')

# brow of right eye/brow unit 
brow = Path(Point(45, -25), Point(65,-15))
rightEyeAndBrow.add(brow)
brow.setBorderWidth(3) # Thicken brow

rightEyeAndBrow.move(0,-25) # Position right eye/brow unit 

# left eye/brow is transformed clone of right
leftEyeAndBrow = rightEyeAndBrow.clone()
leftEyeAndBrow.flip(180)
face.add(leftEyeAndBrow)

# nose is a path with two lines
nose = Path(Point(0,-15), Point(20,15), Point(0,15))
face.add(nose)

# mouth is a filled asymmetric triangular polygon 
mouth = Polygon(Point(-50,35), Point(10,60), Point(50,35))
face.add(mouth)
mouth.move(-1,-1.25)
mouth.setFillColor('darkorchid')

# Move initial face to upper left corner
face.moveTo(100,80)

# face2 is transformed face in lower left corner
face2 = face.clone()
face2.rotate(-90)
face2.moveTo(160, 400)
face2.scale(2)
world.add(face2)

# face3 is transformed face in uppper right corner
face3 = face.clone()
face3.rotate(-90)
face3.scale(0.8)
face3.moveTo(736,80)
world.add(face3)

# face4 is transformed face in lower right corner
face4 = face.clone()
face4.scale(1.5)
face4.rotate(135)
face4.moveTo(600,400)
world.add(face4)

###############################################################################
# Below, summarize your bug fixes using variables named bug1, fix1,
# bug2, fix2, etc. that are assigned to triple-quoted strings,
# as explained in the Task 1 description.
###############################################################################

bug1 = '''The left eye/eyebrow section of the face in the top left corner is not
        facing correctly (line 40).'''
fix1 = '''Instead of rotating leftEyeAndBrow by 180, flip it by 180. Line 40
        should look like leftEyeAndBrow.flip(180).'''

bug2 = '''The mouth is not directly under the rest of the face (line 48).'''
fix2 = '''Add a mouth.move(-1,-1.25) after line 49 but before line 50. '''

bug3 = '''When the face layer is cloned, the mouth does not appear (line 49).'''
fix3 = '''Instead of adding the mouth to the world layer, add it to the face.
        face.add(mouth)'''

bug4 = '''The second face, when cloned, is not scaled (2x) or placed (in bottom
        left corner) according to the instructions (line 58).'''
fix4 = '''After line 56, add face2.scale(2) and change line 58 to 
        face2.moveTo(160,400).'''

bug5 = '''The third face (upper right corner) does not appear (Line 65).'''
fix5 = '''Flip the parameters inside of face3.moveTo(80,736) to 
        face3.moveTo(736,80).'''

bug6 = '''While the fourth face is cloned and scaled properly,
        it still does not show up (72).'''
fix6 = '''Add face4 to the world layer--world.add(face4). Also, change the 
        degree of rotation in line 71 to 135.'''

bug7 = '''After debugging the previous bug, not all of the fourth face shows
        up (Line 72).'''
fix7 = '''Change Line 72 to face4.moveTo(600,400).'''

