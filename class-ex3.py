# 建立實體物件 - 實體屬性 - 實體方法
# File
class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open (self.name, mode="r+", encoding="utf-8")
    def write(self, txt):
        self.file.write(txt)
    def read(self):
        return self.file.read()
# 讀取第一個檔案
file1 = File("other file/test1.txt")
file1.open()
data = file1.read()
print(data)
print("-"*30)

file1.write("test")
file1.open()
data1 = file1.read()
print(data1)
print("-"*30)
# 讀取第二個檔案
#file2 = File("other file/test2.txt")
#file2.open()
#data = file2.read()
#print(data)