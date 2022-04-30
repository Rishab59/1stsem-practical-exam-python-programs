ch = input("Do you want to use temperory variable or not ? \nType 'yes' to use : ")
if (ch =="yes" or ch =="Yes" or ch == "YES"):
    '''
    Swap values
    Algorithm: ( using temporary variable)
    Step 1:Start
    Step 2:Read the values of a,b
    Step 3:swap the values using temporary variable
    Step 4: print the value of a,b
    Step 5: Stop
    '''
    print("using temporary variable :")
    a=eval(input('Enter number 1: '))
    b=eval(input('Enter number 2: '))
    c=a
    a=b
    b=c
    print('The values after swaping ',a,b)
else :
    '''
    Algorithm:(without temporary variable)
    Step 1:Start
    Step 2:Read the values of a,b
    Step 3:swap the values without using temporary variable
    Step 4: print the value of a,b
    Step 5: Stop
    '''
    print("Without using temporary variable")
    a=eval(input('Enter number 1: '))
    b=eval(input('Enter number 2: '))
    a,b=b,a
    print('The values after swaping ',a,b)
