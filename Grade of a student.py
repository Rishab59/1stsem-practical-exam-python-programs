print("\nPROGRAM TO PRINT THE GRADE OF A STUDENT\n")
'''
Grade of a student
Algorithm:
Step 1:Start
Step 2:Read the value of 'marks'
Step 3:check if marks is less than 45 then
Step 4: print better luck next time
Step 5 :else check if marks is greater than or equal to 91
Step 6:print O grade
Step 7:else check if marks is greater than or equal to 81
Step 8: print A grade
Step 9:else check if marks is greater than or equal to 71
Step 10: print B grade
Step 11:else check if marks is greater than or equal to 61
Step 12: print C grade
Step 13:else check if marks is greater than or equal to 51
Step 14: print D grade
Step 15:else check if marks is greater than or equal to 45
Step 16: print E grade
Step 17: Stop
'''
flag = 1
while flag == 1 :
    name = input("Enter student name : ")
    marks = int(input("Enter the mark scored by {} : ".format(name)))
    if marks < 45 :
        print("\nBetter luck next time {}".format(name))
    else :
        if marks >= 91:
            print("\n O grade")
        else :
            if marks >= 81:
                print("\n A grade")
            elif marks >= 71:
                print("\n B grade")
            elif marks >= 61 :
                print("\n C grade")
            elif marks >= 51:
                print("\n D grade")
            elif marks >= 45:
                print("\n E grade")
            print("Try to improve yourself even more {}".format(name))
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