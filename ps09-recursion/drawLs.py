# Your name: Anika Shields
# Your username: ashields
# CS111 Spring 2018 PS09
# drawLs.py
# Submission date: 4/23/18

from turtle import *

#------------------------------------------------------------------------------
def draw1L(size):
    fd((size*2)/3.0)
    lt(90)
    fd(size/3.0)
    lt(90)
    fd(size/3.0)
    rt(90)
    fd((size*2)/3.0)
    rt(90)
    bk(size/3.0)
    rt(90)
    fd(size)
    lt(90)
    
def drawLs(size, level):
    """Draw recursive L pattern as specified"""
    if level > 0:
        #drawing initial L
        draw1L(size)
        
        #getting into position for first recursive call 
        #(creates L on right side of initial L)
        fd((size*2)/3.0)
        drawLs(size/2.0, level-1.0)
        bk((size*2)/3.0)
        
        #getting into position for second recursive call
        #(creates L on upper left side of initial L)
        lt(90)
        fd(size)
        rt(90)
        drawLs(size/2.0, level-1.0)
        lt(90)
        bk(size)
        rt(90)
        

# You may also define any helper functions you find useful


#------------------------------------------------------------------------------
# -- do not change these functions  ---    
def initializeTurtle():
    """initialize turtle on canvas before drawing"""
    # setup(800,600) # Create a turtle window 
    setup(400,500) # Create a turtle window 
    reset() # Show turtle window and turtle
    pencolor('red')
    
    # Set the speed; 0=No animation, 1=slowest, 6=normal, 10=fast, etc.
    speed(6) # can change this to vary the speed of your turtle

    #shape("turtle") # Make turtle shape a turtle (as opposed to arrow)
    #Turtle, by default, starts roughly in center of canvas
    
    # Put turtle in bottom left cornerish
    pu() 
    setx(-150)
    sety(-200)
    pd()
    turtleWindowToTop()
   
def run(levels):
  initializeTurtle()
  drawLs(200,levels)
  # done() # Bug in current Canopy: done() causes problems; do *not* invoke it
  
def turtleWindowToTop():
    # Magical statements to make turtle window come to top of screen. 
    # if platform.system() == 'Darwin': # For Macs
    #      os.system('''/usr/bin/osascript -e 'tell app "Finder" to 
    #                 set frontmost of process "Python" to true' ''') 
    root = getscreen()._root
    root.attributes('-topmost', True)

#------------------------------------------------------------------------------
# Testing

if __name__=='__main__':
    '''Add your test cases here'''
    run(3)
   
