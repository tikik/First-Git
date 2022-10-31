#find position of the next occurent:
'''
word = 'Toi khong biet ban la ai'
user_input= str(input('Please guess a char: '))
position = -1
position = word.find(user_input, position +1)
print(position)
#count the number of times the character appear in a string:
num_occ= word.count(user_input)
print(num_occ)
print('abcde'.islower())
print('ABDCDS'.isupper())
print('HTTPS://google.com'.startswith('HTP'))
'''

#check alphabetical letters:
print('LINCOL   '.isupper())
print(' '.isspace())
print('\n \n'.isspace())
