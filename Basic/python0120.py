#----Function----#
#若使用無限參數時的做法如下
#無限參數將以Tuple來儲存

def sum(*nums):
    result = 0
    for i in nums:
        result+=i
    print("sum= ", result)
    print("avg= ", result/len(nums))

sum(1,2,3,4,5,6,7,8,9,10)