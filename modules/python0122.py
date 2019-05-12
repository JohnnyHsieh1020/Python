#----Module 模組----#
#----import----#
import configPy
import sys
print(sys.path)
print('-'*30)
import testModule as tm

#resultD = tm.distance(1, 1, 5, 5)
#print(resultD)
#print('-'*30)

#resultS = tm.slope(1, 2, 5, 6)
#print(resultS)
#print('-'*30)

coordinateD = [int(x) for x in input("Please enter two point's coordinate to calculate the distance: ").split()]

ansD = tm.distance(coordinateD[0], coordinateD[1], coordinateD[2], coordinateD[3])
print(ansD)
print('-'*30)

coordinateS = [int(x) for x in input("Please enter two point's coordinate to calculate the slope: ").split()]

ansS = tm.slope(coordinateS[0], coordinateS[1], coordinateS[2], coordinateS[3])
print(ansS)
print('-'*30)