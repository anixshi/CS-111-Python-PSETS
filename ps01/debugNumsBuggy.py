# *** DO NOT EDIT THIS FILE! ***
# Bud Lojack's buggy debugNumsBuggy.py for CS111 PS01 Task 1

# Tests involving an integer
intNum = raw_input('Enter a nonnegative integer intNum: ')
print('The integer you entered is intNum')
print 'Three times intNum is', intNum * 3
print intNum, 'concatenated copies of X is', intNum+'X'
print 'The integer remainder of',  intNum, 'divided by 3 is', + int(intNum)%3
print 'The integer quotient of', intNum, 'divided by 3 is', int(intNum/3)
print 'The floating point quotient of', intNum,\
      'divided by 3 is', float(int(intNum)/3)
print 'The number of digits in', intNum, 'is', len(int(intNum))

# Tests involving an floating point number
floatNum = raw_input('Enter a floating point number floatNum: ')
'floatNum is ' + floatNum
print(floatNum +  ' rounded to two places is ' + round(float(floatNum),2))
print floatNum, 'truncated to an integer is', int(floatNum)
print floatNum, 'rounded to an integer is', round(floatNum)
print 'The maximum of', intNum, 'and', floatNum, 'is', max(intNum, floatNum)