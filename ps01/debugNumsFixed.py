# Your name: Anika Shields
# Your username: ashields
# CS111 PS01 Task 1
# debugNumsFixed.py
# Submission date: Feb 5, 2018

###############################################################################
# CS111 PS01 Task 1
# 
# Initially, this file contains the buggy contents of Bud Lojack's 
# debugNumsBuggy.py file. 
# 
# Your task is to modify this file by finding and fixing as many bugs 
# bugs as you can find. 
# 
# You should summarize all bugs and their fixes by assigning variables
# named bug1, fix1, bug2, fix2 at the end of this file, as explained 
# in the Task 1 description. 
#
###############################################################################

# Tests involving an integer
intNum = raw_input('Enter a nonnegative integer intNum: ')
print 'The integer you entered is', intNum 
print 'Three times intNum is', (int (intNum)) * 3
print intNum, 'concatenated copies of X is', int(intNum) * 'X'
print 'The integer remainder of',  intNum, 'divided by 3 is', + int(intNum)%3
print 'The integer quotient of', intNum, 'divided by 3 is', (int(intNum))/3
print 'The floating point quotient of', intNum,\
      'divided by 3 is', float(intNum)/float(3)
print 'The number of digits in', intNum, 'is', len(intNum)

# Tests involving an floating point number
floatNum = raw_input('Enter a floating point number floatNum: ')
print 'floatNum is', floatNum
print floatNum,'rounded to two places is',round(float(floatNum),2)
print floatNum, 'truncated to an integer is', int(float(floatNum))
print floatNum, 'rounded to an integer is', int(round(float(floatNum)))
print '\n','The maximum of',intNum,'and',floatNum,\
        'is',max(int(intNum),float(floatNum))\

###############################################################################
# Below, summarize your bug fixes using variables named bug1, fix1,
# bug2, fix2, etc. that are assigned to triple-quoted strings,
# as explained in the Task 1 description.
###############################################################################


bug1 = '''Line 6 of debugNumsBuggy.py prints the characters of the string 
        'intNum' rather than the nonnegative integer the program asks for. '''
        
fix1 = '''Change the printed string to say: 
        print 'The integer you entered is', intNum. Writing the string this way
        allows for the program to correctly display the value of intNum.'''
        
bug2 = '''In Line 7, intNum is being concatenated three times instead of
        actually being multiplied by three like the program states. '''
        
fix2 = '''Change the expression in the printed string to 
        (int (intNum)) * 3) so that both intNum and 3 are treated
        as integers. '''
        
bug3 = '''Instead of printing intNum amount of X's in Line 8, the program
        concatenates the two so that it ends up as intNumX.'''

fix3 = '''Change the expression to be (int(intNum))*'X' so that intNum is 
        converted and then treated as an integer and X can be concatenated.'''

bug4 = '''In Line 10, intNum only needs to be converted into an integer since 
        the division operand expects to only be dealing with integers.'''

fix4 = '''Change the expression to be (int(intNum))/3.'''

bug5 = '''In Line 12, the original program contains the expression
        float(int(intNum)/3) which results in a floating point number that
        could be even more exact.'''

fix5= '''Change the expression to be float(intNum)/float(3) so that both
        values can be treated as floating point numbers.'''

bug6 = '''In Line 13, the len function cannot find the length of integers.'''

fix6 = ''' Change the expression to len(intNum).'''

bug7 = '''Line 17 is missing the print function which would allow for the
        statement about floatNum to show.'''

fix7 = '''The print statement should look like 
        print 'floatNum is', floatNum.'''

bug8 = '''Line 18--String and float objects cannot be concatenated in Python 
        because of their different properties.'''

fix8 = '''Change the print statement to say
        print floatNum , ' rounded to two places is ', round(float(floatNum),2).
        Using commas instead of the addition symbol will help Python avoid 
        mistaking the float function as a string object.'''

bug9 = '''Before floatNum can be truncated to an integer in Line 19, it needs
        to be converted into an actual floating point number.'''

fix9 = '''Change the expression to int(float(floatNum)).'''

bug10 = '''In order to be rounded to an integer in Line 20, floatNum needs to be
        be converted into a float number. The int function helps in removing 
        the decimal point and the following numbers so floatNum can be presented
        as a decimal number.'''

fix10 = '''Change the expression to int(round(float(floatNum))).''' 

bug11 = '''The max function does not give the value that the user expects in 
        Line 21. It gives the minimum number instead.''' 

fix11 = '''intNum and floatNum need to be converted into actual integers and
        floating point numbers before they can be compared in a max function.
        The expression should now be max(int(intNum),float(floatNum)).'''
        
bug12 = '''There is a blank line that should be printed before Line 21 that
        is missing.'''

fix12 = '''Add 'n\' after the print function but before the statement. '''
