print("PROGRAM TO FIND THE FACTORIAL OF A NUMBER USING RECURSION")
'''
Factorial of a number using recursion
Algorithm:
Step 1:Start
Step 2:Read the number n
Step 3:call factorial(n)
Step 4: print factorial f
Step 5: Stop
factorial(n)
Step 1:If n==1 then return 1
Step 2: Else f =n*factorial(n-1)
Step 3: return f
'''
flag = 1
while flag == 1 :
    def fact(n):
        if n == 0 :
            return 1
        return n*fact(n-1)
    n = int(input("Enter a number :"))
    print('Factorial of {} is {}'.format(n,fact(n)))
    print("----------------------------------------------------------")
    ch = input("Do you want to continue \nType yes to continue :\t")
    chli= ["yes","Yes","YES","y","Y"]
    if ch in chli :
        print("----------------------------------------------------------")
    else :
        flag = 0
        print("----------------------------------------------------------")
        print("Thank You ! ")
        print("----------------------------------------------------------")
input()