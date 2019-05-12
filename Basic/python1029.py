#----int----#
print("---------int---------")
a=123
print(a)
print(type(a))
#-----------#

#----str----#
print("---------str---------")
b='123'
print(b)
print(type(b))
#-----------#

#----list(有順序、可動的列表)----#
print("---------list---------")
c=[1,2,3]
print(c)
print(type(c))
#-----------#

#----tuple(有順序、不可動的列表)----#
print("---------tuple---------")
d=(1,2,3)
print(d)
print(type(d))
#-----------#

#----float----#
print("---------float---------")
e=1.23
print(e)
print(type(e))
#-----------#

#----set(沒有順序)----#
#---- & 表示交集 ----#
#---- | 表示聯集 ----#
#---- - 表示差集 ----#
#---- ^ 表示反交集 取不重複的 ----#
#----除了 in 之外 也可以使用 not in----#
print("---------set---------")
f={1,2,3}
s={2,4,6}

print(f)
print(type(f))
print(3 in f)

r=f & s 
print(r)

w=set("hello") #---- 將再拆成h e l o(重複的字只顯示一次) ----#
print("h" in w)
#-----------#

#----dictionary----#
#----可使用 in 以及 not in 判斷 key 是否存在----#
print("---------dictionary---------")
f={"apple":"蘋果","hello":"你好"}
print(f)
print(type(f))
dic={x:x*2 for x in [3,4,5]}
print(dic)
#-----------#