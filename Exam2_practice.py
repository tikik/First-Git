user_input = input('What are the numbers?')
tokens = user_input.split()
nums = []
for r in tokens:
    nums.append(int(r))

print()
#print each position and its value:
for order in range(len(nums)):
    value = nums[order]
    print(f'{order}: {value}')

#determine maximum even number:
max_num = None
for m in nums:
    #first even number found:
    if max_num == None and m % 2 == 0:
        #first even number found
        max_num = m
    elif (max_num != None) and (m > max_num) and m % 2 == 0:
        #larger even number found
        max_num = m
print('Max even #:', max_num)


user_input = input('Enter numbers: ')
tokens = user_input.split()

#convert string to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(tokens))
    print(f'{pos}: {token}')
sum = 0
for num in nums:
    sum += num
print('Sum:', sum)
#built in function for list iteration:
print(all([1,4,5,6]))
#this should return TRUE all(list) return every element is tRUE, or not 0.
#any(list) : if any element is TRUE
#max(list): get maximum ele in the list
#min(list): get min ele in the list
#sum(list): get sum of all ele.
#'90 92 94 95'
