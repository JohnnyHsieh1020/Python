#----List----#
    #----append(n) 加在最後面----# 
    #----insert(i,n) n加在位置i前面----# 
    #----pop(n) 若括號內無值=>最後一個丟掉；若有值=>丟掉第n個位置的值----# 
    #----remove(n) 將list中第一個出現的n移除----# 
    #----clear() 將list的值全部移除----# 
    #----可搭配使用 max() min() sum()----#
    #----split()預設值是將空格、\n、\t 進行分隔----#
#----import----#
import numpy as np
import math
#----Practice1----# 
a=[1,2,3,4,5,2]

for i in range(len(a)):
    a[i]=a[i]*a[i]
    print(a[i], end=' ')
print('\n')
print(a)

#----append(n) 加在最後面----# 
a.append(10)
print(a)
#----insert(i,n) n加在位置i前面----# 
a.insert(2,11)
print(a)
#----pop(n) 若括號內無值=>最後一個丟掉；若有值=>丟掉第n個位置的值----# 
a.pop(4)
print(a)
#----remove(n) 將list中第一個出現的n移除----# 
a. remove(4)
print(a)
#----可搭配使用 max() min() sum()----#
print('max=', max(a))
print('min=', min(a))
print('sum=', sum(a))
print('\n')

#----Practice2 adjustment score----# 
score=[int(x) for x in input('請輸入五筆成績來做調整(每筆之間請用空白鍵):').split()]

print('五筆成績: ', end=' ')
for i in range(len(score)):
    print(score[i], end=' ')
print('\n')

print('平均成績: ', np.average(score))

print('\n調整後的五筆成績: ', end=' ')
for i in range(len(score)):
    score[i]=round(math.sqrt(score[i])*10, 2)
    print(score[i], end=' ')
print('\n')

print('調整後的平均成績: ', round(np.average(score), 2))
