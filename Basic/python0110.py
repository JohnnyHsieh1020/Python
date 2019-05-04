#----Dict----#
    #----add----#
        #dict={}----#
    #----del----#
        #del dict={key}delete the ordered key value----#
    #----dict.get(key, 'default_value') if there is wrong then print "default_value"----#
#----import----#
import random 
from itertools import repeat
#----Practice1-Add dict----#
newDict={}

for i in range(0,3):
    k=input('Please enter the key: ')
    v=int(input('Please enter the corresponding value: '))
    newDict[k]=v
    print(end='\n')

print(newDict)

#----Practice2----#
scoreDict={}
print('Please enter singer and score(5 people)', end='\n')

for i in range(0,5):
    name = input("Singer's name: ")
    score = int(input("Score: "))
    scoreDict[name]=score
    print(end='\n')

print(scoreDict, end='\n')

print('----------------------')
print("Search singer's score", end='\n')
print('----------------------')

for j in repeat(None):
    search=input('Enter the name of the singer:')
    result=scoreDict.get(search, 'default_value')
    if type(result) == int:
        print('%s got %d !' %(search, result), end='\n')
    else:
        print(result, end='\n')
        break
    print(end='\n')