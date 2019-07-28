# Your name: Daphka Alius, Anika Shields
# Your username: dalius, ashields
# CS111 Spring 2018 PS10 Task 2
# recursiveQuilts.py
# Submission date: 5/1/18

from picture import *

#---------------------------- Task 3a quadRecurse -----------------------------
def quadRecurse(pic1, pic2, levels):
    """
    Returns an upper right quadrant of a quilt as shown in the assignment.
    """
    if levels == 0:
        return empty()
    elif levels > 0:
        miniQuadRecurse = quadRecurse(pic2, pic1, levels-1)
        return fourPics(upperLeft(pic2, pic1, levels-1), miniQuadRecurse,
        pic1, flipAcrossDiag(upperLeft(pic2, pic1, levels-1)))
                        
# Define any helper functions used in Task 3a below
def upperLeft(pic1, pic2, levels):
    if levels == 0:
        return empty()
    elif levels > 0:
        miniUpperLeft = upperLeft(pic2, pic1, levels-1)
        return fourPics(miniUpperLeft, miniUpperLeft, pic1, pic1)
    

#------------------------------- Task 3b quilt --------------------------------
# Task 3b
def quilt(pic1, pic2, levels):
    """Returns the quilt pattern in the assignment."""
    if levels == 0:
        return empty()
    elif levels > 0:
        return(rotations(quadRecurse(upperRightNest(pic1, pic2), 
        upperRightNest(pic2, pic1), levels)))
        


#------------------ Provided definitions (do not change these) ----------------
emptyPic = empty()
redLeaves = leaves('red')
greenLeaves = leaves('forestgreen')
pyTri = triangles('purple', 'yellow') # purple-yellow-triangles
gwTri = triangles('forestgreen', 
                  'lightgrey') # green-whiteish(really-greyish)-triangles

#---------------------------------- Test cases --------------------------------
if __name__=='__main__':
    """testing code: uncomment to test"""
    
    ##Ulose all picture windows from previous tests
    closeAllPics()
    
    """test cases for quadRecurse"""
    # displayPic(quadRecurse(pyTri, gwTri, 0))
    # displayPic(quadRecurse(pyTri, gwTri, 1))
    # displayPic(quadRecurse(pyTri, gwTri, 2))
    # displayPic(quadRecurse(pyTri, gwTri, 3))
    # displayPic(quadRecurse(pyTri, gwTri, 4))
    #displayPic(quadRecurse(pyTri, gwTri, 5))
    #displayPic(quadRecurse(pyTri, gwTri, 6)) 
    
    #for levels in range(5):
    #    p = quadRecurse(redLeaves, greenLeaves, levels)
    #    displayPic(p) 

    ##Addressing issue with cs1graphics: sometimes need to display 
    ##a simple picture for the earlier complex one to show up!
    #displayPic(emptyPic)   
    
    ##Use this to close all picture windows. 
    #closeAllPics()
    
    """test cases for quilt"""
    # displayPic(quilt(pyTri, gwTri, 0))
    # displayPic(quilt(pyTri, gwTri, 1))
    # displayPic(quilt(pyTri, gwTri, 2))
    displayPic(quilt(pyTri, gwTri, 3))
    #displayPic(quilt(pyTri, gwTri, 4))
    # Invoking quilt with levels >=4 may cause the program to freeze
    
    #
    #for levels in range(5):
    #    p = quilt(redLeaves, greenLeaves, levels)
    #    displayPic(p)

    ##Addressing issue with cs1graphics: sometimes need to display 
    #a simple picture for the earlier complex one to show up!
    # displayPic(emptyPic)   

    ##Use this to close all picture windows. 
    #closeAllPics()




