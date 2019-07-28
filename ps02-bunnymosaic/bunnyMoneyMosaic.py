# Your name(s): Anika Shields
# Your username(s): ashields
# CS111 PS02 Task 2
# bunnyMoneyMosaic.py
# Submission date: 02/13/18

from cs1graphics import *
from cs1graphicsHelper import *
from graphicsState import *

# Import bunny (from bunny.py) and wedge (from wedge.py)
from bunny import bunny
from wedge import wedge

# Below, add your code to create a canvas containing 
# the Bunny Money Mosaic pattern for the **REQUIRED** Task 2 of PS02

# Creating pink 900x600 canvas as requested
paper = Canvas(900,600,'pink','Bunny Money Mosaic')

# completeBunnyMoney will hold the original bunnyMoney template that will then 
# be cloned and transformed to create the rest of the mosaic.
completeBunnyMoney = Layer()

# bunnyWedge (a layer inside of completeBunnyMoney holds the orange wedge 
# and the bunny seen on both ends of the bill.
bunnyWedge = Layer()
bunnyWedge.add(wedge)
bunnyWedge.moveTo(0,0)
bunnyWedge.add(bunny)
bunny.moveTo(75,120)
completeBunnyMoney.add(bunnyWedge)

bunnyCornerBill = Layer()
bill = Rectangle(600,300)
bill.setFillColor('lightgreen')
bill.setDepth(100)
bill.moveTo(300,150)
bunnyCornerBill.add(bill)
bunnyCornerBill.add(bunnyWedge)
completeBunnyMoney.add(bunnyCornerBill)

# Cloning and transforming bunnyWedge2 to create the bunny & wedge combination
# we see on one corner of the bill.
bunnyInBothCornersBill = Layer()
bunnyInBothCornersBill.add(bunnyCornerBill)
bunnyWedge2 = bunnyWedge.clone()
bunnyWedge2.moveTo(600,300)
bunnyWedge2.rotate(180)
bunnyInBothCornersBill.add(bunnyWedge2)
completeBunnyMoney.add(bunnyInBothCornersBill)

# Creating the pinwheel decoration we see in the middle of each bunny bill.
bunnyPinwheel = Layer()
disc = Circle(75, Point(300,150))
disc.setFillColor('navy')
bunnyPinwheel.add(disc)

bunnyWedge3 = bunnyWedge2.clone()
bunnyWedge3.scale(.25)
bunnyWedge3.moveTo(300,150)
bunnyPinwheel.add(bunnyWedge3)

bunnyWedge4 = bunnyWedge.clone()
bunnyWedge4.scale(.25)
bunnyWedge4.moveTo(300,150)
bunnyWedge4.rotate(90)
bunnyPinwheel.add(bunnyWedge4)

bunnyWedge5 = bunnyWedge.clone()
bunnyWedge5.scale(.25)
bunnyWedge5.moveTo(300,150)
bunnyWedge5.rotate(-90)
bunnyPinwheel.add(bunnyWedge5)

bunnyWedge6 = bunnyWedge.clone()
bunnyWedge6.scale(.25)
bunnyWedge6.moveTo(300,150)
bunnyPinwheel.add(bunnyWedge6)
completeBunnyMoney.add(bunnyPinwheel)

# Adding the grey rectangle that is placed on the bottom of the bill. 
bunnyMoney = Layer()
bunnyMoney.add(bunnyInBothCornersBill)
bunnyMoney.add(bunnyPinwheel)
table = Rectangle(330,70)
table.setFillColor('darkgrey')
table.moveTo(165,265)
bunnyMoney.add(table)
completeBunnyMoney.add(bunnyMoney)

# Creating and transforming five clones of the completeBunnyMoney layer 
# in order to create the mosaic.
money1 = completeBunnyMoney.clone()
money1.scale(1)
money1.rotate(90)
money1.moveTo(900,0)
paper.add(money1)

money2 = completeBunnyMoney.clone()
money2.scale(.75)
money2.rotate(180)
money2.moveTo(600,225)
paper.add(money2)

money3 = completeBunnyMoney.clone()
money3.scale(.5)
money3.rotate(-90)
money3.moveTo(0,300)
paper.add(money3)

money4 = completeBunnyMoney.clone()
money4.scale(1)
money4.moveTo(0,300)
paper.add(money4)

money5 = completeBunnyMoney.clone()
money5.scale(.25)
money5.moveTo(150,225)
paper.add(money5)