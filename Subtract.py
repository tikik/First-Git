a= int(input('Your 1st numbers to subtract:'))
b= int(input('Your 2nd numbers to subtract:'))
try:
    print(a-b)
except ValueError:
    print('Your character was not a number, cannot do subtraction')
print('Stop here. Thank you!')
