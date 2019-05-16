# 建立實體物件 - 實體屬性 - 實體方法
# 座標
class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, x2, y2):
        return(((self.x-x2)**2)+((self.y-y2)**2))**0.5        
p1 = Point(3,4)
p1.show()
result = p1.distance(0,0)
print('distance:', result)
