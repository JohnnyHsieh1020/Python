#----List----#
    #--slice語法：
    # list[start: end]，start(預設為0)和end(len(list))都可以省略不寫
    # list[ :end]代表 0~end-1
    # list[start: ]代表start~len(list)-1
    # list[ : ]代表0~len(list)-1
#----import----#
import numpy as np
import math
#----Practice3----#
a=['hi','hello','yob','hey']
#----印出從第0個位置到第2-1個位置----#
print(a[0:2])
print('----------')
#----印出從第1個位置到最後一個位置----#
print(a[1: ])
print('----------')
#----印出從第1個位置到第3-1個位置----#
print(a[ :3])
print('----------')
#----印出所有的值----#
print(a[ : ])
print('----------')

