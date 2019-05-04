#----For loop----#
#----import----#
import random 
from itertools import repeat
#----Practice1(9*9)----# 
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print(end='\n')

#----Practice2(guess num)----# 
ans=random.randint(0,101)
upper = 100
lower = 0
count = 0

for i in repeat(None):
    num = int(input('Guess a number:'))
    count+=1
    if num == ans:
        print('Correct!')
        break
    elif num > ans:
        upper=num
        print('The number is bigger than the answer (%d ~ %d)' %(lower, upper))
    elif num < ans:
        lower=num
        print('The number is smaller than the answer (%d ~ %d)' %(lower, upper))
print('The answer is ', ans)
print('Game Over')
print('You use %d times to guess' %(count))