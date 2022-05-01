print("\nPROGRAM TO PRINT THE GREATEST OF THREE NUMBER\n")
'''
Largest of three numbers
Algorithm:
Step 1:Start
Step 2:Enter three numbers
Step 3:use the following if condition to find the biggest number
Step 4:if (num1>num2)and(num1>num3) 
        num1 is the largest
Step 5: elif (num2>num3) 
        num2 is the largest
Step 6: else num3 is the largest
Step 7: print the output
Step 8: Stop
'''
flag = 1
while flag == 1 :
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter a number : "))
    n3 = int(input("Enter a number : "))
    if (n1 > n2) and (n1 > n3):
        print("{} is the greater number amoung {} ,{} ,{} ".format(n1,n1,n2,n3))
    elif n2 > n3 :
        print("{} is the greater number amoung {} ,{} ,{} ".format(n2,n1,n2,n3))
    else :
        print("{} is the greater number amoung {} ,{} ,{} ".format(n3,n1,n2,n3))
    print("-----------------------------------------------------------")
    ch = input ("Do you want to know the grade for another student ?\nthen type 'yes' : ")
    chli = ["YES","Yes","yes","y","Y"]
    if ch in chli :
        print("-----------------------------------------------------------")
    else :
        print("-----------------------------------------------------------")
        flag = 0
        print ("Thank You !")
        print("-----------------------------------------------------------")
input()