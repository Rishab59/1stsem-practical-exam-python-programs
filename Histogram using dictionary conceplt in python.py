'''
Fequency of each letter using dictionary
Algorithm:
Step 1:Start
Step 2:Read the input sentence from the user
Step 3:call the function histogram(s)
Step 4:using for loop iterate the keys
Step 5: Stop
'''
flag = 1
while flag == 1 :
    def histogram (s):
        d={}
        for ch in s:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        return d
    s = input('Enter sentence :\n')
    h=histogram(s)
    print("-------------------------------------------------------------")
    print('Frequency of each character in the given sentence :\n',h)
    for k in h.keys():
        print(k,':',h[k]*'*')
    print("-------------------------------------------------------------")
    ch = input('Do you want to do it again ?\nEnter yes to continue or any other input ot exit : ')
    if (ch =="yes" or ch =="Yes" or ch == "YES"):
        flag = 1
        print("-------------------------------------------------------------")
    else :
        flag = 0
        print("Thank you ! ")
