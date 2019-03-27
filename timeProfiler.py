# Anika Shields
# ashields
# CS111 Problem Set 1, Task 2
# timeProfiler.py
# 02/06/18

###############################################################################
# timeProfiler.py is a program "that helps students visualize how they spend  #
# their time during a typical week. The program will ask the user to enter a  # 
# few pieces of information, and then will display a textual representation of#
# the hours they spend in four activities during the week:                    #
# 1. Classwork:                                                               #
# 2. Activities Outside of Class:                                             #
# 3. Sleep:                                                                   #
# 4. Free Time:" (cs111.wellesley.edu).                                       #
###############################################################################

# ask user for name
stuName = raw_input ('What is your name? ')

# ask student for the number of classes they're taking as well as the avg time 
# spent in class (helpful in calculating class hours)
classTaking = raw_input ('How many classes are you taking this semester? ')
avgClass = raw_input ('What is the average time in class per week this'+
' semester? ')
                        
# ask student for name of time they spend outside of class as well as the time
# spent (helpful in calculating 'everything outside of class' time)
outName = raw_input ('What shall we call the \'everything outside of class\'' 
+' category? ')
freeTime = raw_input ('How many hours per week do you spend on \'' + outName +
'\'? ')

# ask student for avg sleep hours (helpful in calculating weekly sleep hours)
sleepTime = raw_input ('How many hours per day do you sleep on average? ')

# calculating weekly time spent in class, outside of class, sleeping, and the
# time that remains
classCalc = float(avgClass)* float(3)* float(classTaking)
sleepCalc = float(sleepTime)*7.0
remainCalc = float(168)-classCalc-float(freeTime)-float(sleepCalc) 

# calculating lengths of hour category titles
length1 = len(str(round(classCalc,2))+' class hours: ')
length2 = len(str(round(float(freeTime),2)) + ' ' + outName + ' hours: ')
length3 = len(str(round(sleepCalc,2)) + ' sleep hours: ')
length4 = len(str(round(remainCalc,2)) + ' free hours: ')

# calculating the amount of spaces the longest hour title has
lenmax = max(length1, length2, length3, length4)
maxshift = lenmax * ' ' 

# weekly time profile displays how user spends their time over the course of 
# a week (168 hours). lenmax-lengthx * ' ' determines the amount of spaces 
# needed to align the colons.

print '\nWeekly time profile for ' + stuName + ':'

print ((lenmax-length1)*' ' + str(round(classCalc,2)) +' class hours: '+
        int(round(classCalc))*'C')
        
print ((lenmax-length2)*' ' + str(round(float(freeTime),2)) + ' ' + outName +
        ' hours: ' + int(round(float(freeTime)))*'X')
        
print ((lenmax-length3)*' ' + str(round(sleepCalc,2)) + ' sleep hours: ' +
        int(round(sleepCalc))*'S')
        
print ((lenmax-length4)*' ' + str(round(remainCalc,2)) +' free hours: ' +
        int(round(remainCalc))*'F')


