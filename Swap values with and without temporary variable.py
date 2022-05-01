print("PROGRAM TO SWAP TWO NUMBERS USING AND WITHOUT USING TEMPORARY VARIABLE\n")
flag = 1
while flag == 1 :
    ch = input("Do you want to use temperory variable or not ? \nType 'yes' to use : ")
    chli = ["yes","Yes","YES","y","Y"]    
    if ch in chli :
        '''
        Swap values
        Algorithm: ( using temporary variable)
        Step 1:Start
        Step 2:Read the values of a,b
        Step 3:swap the values using temporary variable
        Step 4: print the value of a,b
        Step 5: Stop
        '''
        print("\nUsing temporary variable :\n")
        a = int(input('Enter number 1: '))
        b = int(input('Enter number 2: '))
        c = a 
        a = b
        b = c
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
        print("\nWithout using temporary variable : \n")
        a = int(input('Enter number 1: '))
        b = int(input('Enter number 2: '))
        a,b = b,a
        print('The values after swaping ',a,b)
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