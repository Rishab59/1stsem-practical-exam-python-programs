print("\nPROGRAM TO FIND THE GCD OF TWO NUMBERS\n")
'''
GCD using recursion
Algorithm:
Step 1:Start
Step 2:Read num1 and num2
Step 3:call gcd(m,n)
Step 4: print gcd
Step 5: Stop
gcd(m,n)
Step 1: check whether n==0 return m
Step 2 :else return gcd (n , m%n)
'''
flag = 1
while flag == 1 :
    def gcd(m,n):
        if m < n :
            m,n = n,m
        if n == 0 :
            return m
        else: 
            return gcd(n,m%n)
    n1 = eval(input('Enter first number :'))
    n2 = eval(input("Enter second number : "))
    print("GCD of {} and {} is {}".format(n1,n2,gcd(n1,n2)))
    print("----------------------------------------------------------")
    ch = input("Do you want to continue \nType yes to continue :\t")
    chli = ["yes","Yes","YES","y","Y"]
    if ch in chli :
        print("----------------------------------------------------------")
    else :
        flag = 0
        print("----------------------------------------------------------")
        print("Thank You ! ")
        print("----------------------------------------------------------")
input()