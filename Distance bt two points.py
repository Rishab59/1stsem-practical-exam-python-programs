import math
print ('\nPROGRAM TO FIND THE DISTANCE BETWEEN TWO POINS\n')
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
flag = 1
while flag == 1 :
    x1 = eval(input('Enter the value of x1 : '))
    y1 = eval(input('Enter the value of y1 : '))
    x2 = eval(input('Enter the value of x2 : '))
    y2 = eval(input('Enter the value of y2 : '))
    print('The Distance between ({},{}) and ({},{}) is {}'.format(x1,y1,x2,y2,(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))))
    print("-----------------------------------------------------------")
    ch = input ("Do you want to know the grade for another student ?\nthen type 'yes' : ")
    chli = ["YES","Yes","yes","y","Y"]
    if ch in chli :
        print("-----------------------------------------------------------")
    else :
        flag = 0
        print("-----------------------------------------------------------")
        print ("Thank You !")
        print("-----------------------------------------------------------")
input()