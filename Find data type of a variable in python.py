print("\nPROGRAM TO FIND THE DATA TYPE OF A VARIABLE\n")
'''
Data types
Algorithm:
INPUT : x
OUTPUT : to display different type of data types
Step 1:Start
Step 2:Read the value of x
Step 3:use type()function , which returns the data type of the variable passed.
Step 4: print the output
Step 5: Stop
'''
flag = 1
while flag == 1 :
    x = eval(input("Enter some data who's data type has to be seen :\t"))
    print("The data type of {} is {} ".format(x,type(x)))
    print("----------------------------------------------------------")
    ch = input("Do you want know the data type of another data\nType yes to continue :\t")
    chli = ["yes","Yes","YES","y","Y"]
    if ch in chli :
        print("----------------------------------------------------------")
    else :
        flag = 0
        print("----------------------------------------------------------")
        print("Thank You ! ")
        print("----------------------------------------------------------")
input()