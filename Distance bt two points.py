'''
Distance between two points
INPUT : x1,y1,x2,y2
OUTPUT:Distance between two points.
Algorithm:
Step 1 : Start
Step 2: import math module
Step 3: Read values x1,y1,x2,y2
Step 4:Calculate the distance using the formula
        math.sqrt((x2-x1)**2+(y2-y1)**2) and store the result in distance
Step 5: Print distance
Step 6:Stop
'''
import math
num1=eval(input('Enter the number A : '))
num2=eval(input('Enter the number B : '))
num3=eval(input('Enter the number C : '))
num4=eval(input('Enter the number D : '))
distance = math.sqrt(((num1-num3)**2)+((num2-num4)**2))
print('The Distance is ',distance)
