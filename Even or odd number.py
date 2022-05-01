print("\nPROGRAM TO PRINT THE GIVEN NUMBER EVEN OR ODD\n")
'''
Check whethe even or odd using if...else
Algorithm:
Step 1:Start
Step 2:Read the number
Step 3:using if condition check the value is even or odd number
Step 4: print the output
Step 5: Stop
'''
flag = 1
while flag == 1 :
    num = int(input("Enter a number :"))
    if num % 2 == 0 :
        print("{} is an even number".format(num))
    else :
        print("{} is a odd number".format(num))
    print("----------------------------------------------------------")
    ch = input("Do you want to continue \nType yes to continue :\t")
    chli = ["yes","Yes","YES","y","Y"]
    if ch in chli:
        print("----------------------------------------------------------")
    else :
        flag = 0
        print("----------------------------------------------------------")
        print("Thank You ! ")
        print("----------------------------------------------------------")
input()