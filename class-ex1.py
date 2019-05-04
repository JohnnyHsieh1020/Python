# 建立實體物件 - 實體屬性
class Fullname: # 類別
    def __init__(self, first, last): #__init__ 初始化函式
        self.first = first #透過 self 定義定義實體屬性
        self.last = last
# 建立第一個實體物件    
name1 = Fullname("C.C.", "Hsieh") # call class
print(name1.first, name1.last)

# 建立第二個實體物件
fname = input("What is your first name?")
lname = input("What is your last name?")  
name2 = Fullname(fname, lname)
print(name2.first, name2.last)      