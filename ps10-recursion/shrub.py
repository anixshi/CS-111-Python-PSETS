# Your name: Anika Shields
# Your username: ashields
# CS111 Spring 2018 PS10 Task 1
# shrub.py
# Submission date: 5/1/18

from turtle import *

#----------------------- Define your shrub function here ----------------------
def shrub(trunkLength, angle, shrinkFactor, minLength):
    """
    Draws a shrub with the specified parameters.
    Returns a pair (a 2-tuple) consisting of 
      (1) the total number of branches (including the trunk) and
      (2) the total length of the branches (including the trunk)
    of the shrub
    """
    
    if trunkLength < minLength:
        return (0,0)
    
    else:
        #getting into position to draw trunk
        fd(trunkLength) 
        
        #Drawing right branch(1st recursive call)
        rt(angle)       
        numBranchesRight, branchLenRight = shrub((trunkLength*shrinkFactor), 
                                                angle, shrinkFactor, minLength)
        
        #Drawing left branch(2nd recursive call)
        lt(angle*2)
        numBranchesLeft, branchLenLeft = shrub(
                                (trunkLength*shrinkFactor*shrinkFactor), angle, 
                                    shrinkFactor, minLength)
        
        #Going back to tree trunk
        rt(angle); bk(trunkLength)
    
        
        return (numBranchesRight + 1 + numBranchesLeft, 
                                branchLenRight + branchLenLeft + trunkLength)

#------------------- Testing functions (do not change these) ------------------

def initialize_turtle():
    """initialize turtle on canvas before drawing"""
    setup(600,600) # Create a turtle window 
    reset() # Clear any existing turtle drawings 
            # and reset turtle position & heading. 
    pensize(1) # Choose a pen thickness  
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal  

    #shape("turtle") # Make turtle shape a turtle (as opposed to arrow)
    #Turtle, by default, starts roughly in center of canvas
    
    # Move turtle to lower middle pointing up 
    pu()
    setpos(0, -(window_height()/2.0 - 20))
    setheading(90)
    pd()
    
    # Magical statement to make turtle window come to top of screen.                              
    getscreen()._root.attributes('-topmost', True)
    
def testShrub (trunkLength, angle, shrinkFactor, minLength):
    """Testing code for shrub function that initializes screen and turtle,
        calls shrub, and returns (not prints) the result."""
    testInputString = ('shrub(' + str(trunkLength) + ', ' 
                       + str(angle) + ', ' + str(shrinkFactor) 
                       + ', ' + str(minLength) + ')')


    # Put testInputString in title at top of window
    title(testInputString)    
    initialize_turtle() # In Fall 2016, need to call reset() *after* setting
                        # title in order for it to take effect. 

    result = shrub(trunkLength, angle, shrinkFactor, minLength) 
 
    # A Bug in Fall 2016 Canopy won't change title until reset() or write() 
    # is called,      
    testOutputString = testInputString + ' -> ' + str(result)
    ## Put testOutputString in title at top of window 
    title(testOutputString)

    # Write the result at the turtle
    # It turns out that write causes the title to redisplay!
    write('  ' + str(result), align='left',font=("Arial", 18, "normal"))  
     
    # done() # Bug in current Canopy: done() and exitOnClick cause problems, 
    # so do *not* invoke them
    
    return result
    
def testShrubPrint(trunkLength, angle, shrinkFactor, minLength):
    '''Like testShrub, but prints the result rather than returning it'''
    testInputString = ('shrub(' + str(trunkLength) + ', ' 
                       + str(angle) + ', ' + str(shrinkFactor) 
                       + ', ' + str(minLength) + ')')
    print testInputString, '->', testShrub(trunkLength, angle, 
                                           shrinkFactor, minLength)

# ---------------------------------- Test cases --------------------------------
         
if __name__=='__main__':
    """testing code: uncomment to test"""
    
    # Uncomment each of the lines below to test. 
    # You can only run one invocation of testShrub at a time.

    testShrubPrint(100, 15, 0.8, 50) # expect result (7, 461.6)    
    testShrubPrint(100, 15, 0.8, 40) # expect result (12, 666.4000000000001)
    testShrubPrint(100, 30, 0.82, 40) # expect result (12, 707.95128)
    testShrubPrint(200, 90, 0.75, 40) # expect result (20, 1524.21875)

    # The following test cases take too long to include them in Codder
    # but you should try them manually 
    #testShrubPrint(100, 15, 0.8, 10) # expect result (232, 3973.9861913600025)
    #testShrubPrint(100, 30, 0.82, 10) # expect result (376, 6386.440567704483)
    #testShrubPrint(200, 90, 0.75, 10) # expect result (232, 5056.675148010254)

