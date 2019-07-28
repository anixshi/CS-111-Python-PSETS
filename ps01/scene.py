# Anika Shields and Peggy Wang
# ashields and zwang11
# CS111 Problem Set 1
# scene.py
# 02/04/18

from cs1graphics import *
paper = Canvas(500,700,'cyan3','Totoro by the Pond')

bodyTop = Ellipse(250, 350, Point(250, 300))
bodyTop.setFillColor('dimgrey')
bodyTop.setBorderColor('dimgrey')
paper.add(bodyTop)

bodyBottom = Circle(155, Point(250, 350))
bodyBottom.setFillColor('dimgrey')
bodyBottom.setBorderColor('dimgrey')
paper.add(bodyBottom)

belly = Circle(125, Point(250,400))
belly.setFillColor('khaki1')
paper.add(belly)

foot1 = Ellipse(50, 75, Point(175, 500))
foot1.setFillColor('dimgrey')
foot1.setBorderColor('slategrey')
foot1.setBorderWidth(5)
paper.add(foot1)

foot2 = Ellipse(50, 75, Point(325, 500))
foot2.setFillColor('dimgrey')
foot2.setBorderColor('slategrey')
foot2.setBorderWidth(5)
paper.add(foot2)

ear1 = Polygon(Point(170,150), Point(230, 150), Point(200,60))
ear1.setFillColor('dimgrey')
ear1.setBorderColor('dimgrey')
paper.add(ear1)

ear2 = Polygon(Point(270,150), Point(330, 150), Point(300,60))
ear2.setFillColor('dimgrey')
ear2.setBorderColor('dimgrey')
paper.add(ear2)

eye1 = Circle(15, Point(200, 200))
eye1.setFillColor('white')
paper.add(eye1)

eye2 = Circle(15, Point(300, 200))
eye2.setFillColor('white')
paper.add(eye2)

pupil1= Circle(7, Point(200, 200))
pupil1.setFillColor('black')
paper.add(pupil1)

pupil2= Circle(7, Point(300, 200))
pupil2.setFillColor('black')
paper.add(pupil2)

nose = Polygon (Point(235,220), Point(265, 220), Point(250, 230))
nose.setFillColor('black')
paper.add(nose)

mouth = Path(Point(242, 250), Point(258, 246))
paper.add(mouth)

background = Ellipse(400, 600, Point(250, 250))
background.setFillColor('cadetblue2')
background.setBorderColor('cadetblue2')
background.setDepth(100)
paper.add(background)

bench1 = Rectangle (500, 40, Point(250, 500))
bench1.setFillColor('brown')
bench1.setBorderColor('brown')
bench1.setDepth(80)
paper.add(bench1)

pond = Rectangle(500,200, Point(250, 620))
pond.setFillColor('blue')
pond.setDepth(80)
paper.add(pond)

leafHat = Image ('leaf_hat2 (2).gif')
leafHat.moveTo(250,130)
leafHat.setDepth(1)
paper.add(leafHat)

#bubbles in the pond
bubble1 = Circle (10, Point(375, 650))
paper.add(bubble1)

bubble2 = Circle (10, Point(390, 625))
paper.add(bubble2)

bubble3 = Circle (15, Point(400, 590))
paper.add(bubble3)

name = Text ('My name is Totoro',18)
name.setFontColor('chartreuse3')
name.moveTo(250, 50)
paper.add(name)

#belly design
triangle1 = Polygon(Point(200, 310), Point(225, 310), Point(215, 300))
triangle1.setFillColor('dimgrey')
paper.add(triangle1)

triangle2 = Polygon(Point(235, 310), Point(260, 310), Point(250, 300))
triangle2.setFillColor('dimgrey')
paper.add(triangle2)

triangle3 = Polygon(Point(270, 310), Point(295, 310), Point(285, 300))
triangle3.setFillColor('dimgrey')
paper.add(triangle3)

triangle4 = Polygon(Point(215, 330), Point(240, 330), Point(225, 320))
triangle4.setFillColor('dimgrey')
paper.add(triangle4)

triangle5 = Polygon(Point(250, 330), Point(275, 330), Point(260, 320))
triangle5.setFillColor('dimgrey')
paper.add(triangle5)