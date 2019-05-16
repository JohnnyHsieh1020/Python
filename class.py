# Class類別、定義、使用
# 定義
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("404 Not Found")
        elif src == "file":
            with open ("other file/test2.txt", mode="r", encoding="utf-8") as file:
                data = file.read()
            print(data)
        else:
            print("Read from", src)
# 使用
print(IO.supportedSrcs)
word = input("What do you want to read? ")
IO.read(word)