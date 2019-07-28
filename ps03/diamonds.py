# Your name: Anika Shields
# Your username: ashields
# CS111 PS03 Task 1
# diamonds.py
# Submission date: 2/20/18

#******************************************************************************
# Pre-defined strings. You're not allowed to create any other new strings 
# with quotes in this program!

zeroStar  = '     '
oneStar   = '  *  '
twoStar   = ' * * '
threeStar = '* * *'
empty     = ''

#******************************************************************************
# Define your functions (diamondPattern and other necessary helper 
# functions) below


def printOut(diamondPat):
    print diamondPat
    
    ''' printOut prints out the contents of diamondPatOut and diamondPatIn.'''
def diamondPatOut():
    
    '''diamondPatOut() is a helper function that creates the first, third, 
    fifth, and seventh rows of diamonds.'''
    
    printOut(oneStar + zeroStar + oneStar + zeroStar + oneStar + zeroStar 
            + oneStar) 
    printOut (twoStar + zeroStar + twoStar + zeroStar + twoStar + zeroStar 
            + twoStar)
    printOut (threeStar + zeroStar + threeStar + zeroStar + threeStar + zeroStar + 
            threeStar)
    printOut (twoStar + zeroStar + twoStar + zeroStar + twoStar + zeroStar 
            + twoStar)
    printOut (oneStar + zeroStar + oneStar + zeroStar + oneStar + zeroStar 
            + oneStar) 
        

def diamondPatIn():
    
    '''diamondPatIn() is a helper function that creates the rows of diamonds 
    that are indented.'''
    
    printOut (zeroStar + oneStar + zeroStar + oneStar + zeroStar + oneStar + 
            zeroStar + oneStar)
    printOut (zeroStar + twoStar + zeroStar + twoStar + zeroStar + twoStar + 
            zeroStar + twoStar)
    printOut (zeroStar + threeStar + zeroStar + threeStar + zeroStar + threeStar + 
            zeroStar + threeStar)
    printOut (zeroStar + twoStar + zeroStar + twoStar + zeroStar + twoStar + 
            zeroStar + twoStar)
    printOut (zeroStar + oneStar + zeroStar + oneStar + zeroStar + oneStar + 
            zeroStar + oneStar)


def diamondPattern():
    
    '''diamondPattern() combines both diamondPatOut and diamondPatIn to 
    create the diamond pattern as requested.'''
    
    diamondPatOut()
    diamondPatIn()
    diamondPatOut()
    diamondPatIn()
    diamondPatOut()
    diamondPatIn()
    diamondPatOut()
    diamondPatIn()
    
# Be sure to use meaningful function names, parameter names, and 
# variable names. 

# Comment your code appropriately
# In particular, every function definition should have a 
# triple-quoted docstring between the header and the body
# that briefly explains what the function does.



#******************************************************************************
# Testing block. Put all testing code indented inside this if block
# Uncomment existing calls inside this testing block to run them
# when you press the green run function in Canopy. 

if __name__ == "__main__":
   '''All your testing code should go below.
      Uncomment and comment particular lines as appropriate.'''
   #diamondPattern()
