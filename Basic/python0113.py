#----Function----#
#----語法----#
# def funcName(value):
#   content
#   return int,str,boolean,none(or other kinds of type)

#----function-printMsg----#
def printMsg(msg):
    return msg

#----function-Add1----#
def add(n1, n2):
    result=n1+n2
    return result

#----function-Add2連加----#
def sigma(num):
    sigmaResult=0

    for i in range(1, num+1):
        sigmaResult+=i
  
    return sigmaResult
#----function-printMsg result----#
print(printMsg("Hello world"))

#----function-Add1 result----#
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
print('The answer is', add(a,b))

#----function-Add2 result----#
c= int(input("enter the third number: "))
print('The answer is', sigma(c))