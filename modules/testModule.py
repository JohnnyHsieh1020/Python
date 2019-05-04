#----Module 模組----#
#----import----#
import math

#----計算兩點距離----#
def distance (x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

#----計算斜率----#
def slope (x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)