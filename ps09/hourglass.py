# Your name: Anika Shields  
# Your username: ashields
# CS111 Spring 2018 PS09
# hourglass.py
# Submission date: 4/23/18

#------------------------------------------------------------------------------
# Task 1
# hourglass shapes drawn from alternating rows of characters

def hourglass(numSpaces, size, char1, char2):
    """Prints an hourglass with alternating rows of characters"""
    if size >= 3:
        print numSpaces * ' ' + char1*size
        hourglass(numSpaces+1, size-2, char2, char1)
        print numSpaces * ' ' + char1*size
    elif size == 1 or size ==2:
        print numSpaces * ' ' + char1*size

#------------------------------------------------------------------------------
# Testing 

if __name__=='__main__':
    """testing code: uncomment to test"""
    # hourglass(0, 1, 'A', 'B')
    # hourglass(0, 2, 'C', 'D')
    # hourglass(0, 1, 'A', 'B')
    # hourglass(0, 2, 'C', 'D')
    # hourglass(4, 1, 'E', 'F')
    # hourglass(7, 2, 'G', 'H')
    # hourglass(9, 0, 'I', 'J') # Nothing printed for this case
    # hourglass(3, -17, 'K', 'L') # Nothing printed for this case
    # hourglass(5, 7, '*', '-')
    # hourglass(0, 11, '&', '%')
    # hourglass(0, 12, 'x', 'o')


