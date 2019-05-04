#----int----#
a=123
print(a)
print(type(a))
print("------------------")

#----str----#
b='123'
print(b)
print(type(b))
print("------------------")

#----list(有順序、可動的列表)----#
c=[1,2,3]
print(c)
print(type(c))
print("------------------")

#----tuple(有順序、不可動的列表)----#
d=(1,2,3)
print(d)
print(type(d))
print("------------------")

#----float----#
e=1.23
print(e)
print(type(e))
print("------------------")

#----set(沒有順序)----#
#---- & 表示交集 ----#
#---- | 表示聯集 ----#
#---- - 表示差集 ----#
#---- ^ 表示反交集 取不重複的 ----#
f={1,2,3}
s={2,4,6}
r=f & s 
w=set("hello") #---- 將再拆成h e l o(重複的字只顯示一次) ----#

print(f)
print(type(f))
print(3 in f)
#----3 有沒有在 f 裡面----#
#----除了 in 之外 也可以使用 not in----#

print(r)

print("h" in w)
print("------------------")

#----dictionary----#
#----可使用 in 以及 not in 判斷 key 是否存在----#
f={"apple":"蘋果","hello":"你好"}
print(f)
print(type(f))
dic={x:x*2 for x in [3,4,5]}
print(dic)
print("------------------")




