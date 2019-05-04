#----input pracetice----#
#----Practice1----# 
a=input()
print('a= ',a)

b=input()
print('your name is' , b + '.')

#----Practice2----# 
a= int(input('Please enter a value: '))
b= int(input('Please enter another value: '))

print('a+b= ', a+b)
print('a-b= ', a-b)
print('a*b= ', a*b)
print('a/b= ', a/b)

#----Practice3----# 
x= input('請輸入運符號(+,-,*,/):')
a= int(input('Please enter a value: '))
b=int(input('Please enter another value: '))

if x=='+':
    print('a+b= ', a+b)
elif x=='-':
    print('a-b= ', a-b)
elif x=='*':
    print('a*b= ', a*b)
elif x=='/':
    print('a/b= ', a/b)
else:
    print('error')