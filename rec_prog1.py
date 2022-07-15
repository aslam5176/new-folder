####TO DECREASE NUMBERS IN RRECURSION
a = 90
def recursion(a):
    print(a)
    if(a == 0):
        pass
    else:
        recursion(a - 9)
recursion(a)
####to reverse the number using recursion
##a=int(input("enter the number :"))
##def rec_num(a):
##    print(a)
##    if(a==0):
##        return
##    else:
##        rec_num(a-1)
##rec_num(a)

## TO ADD THE NUMBER IN RECURSION       
##b=int(input("enter the number"))
##count=0
##def rec_num(b):
##    global count
##    count+=1
##    print(count)
##    if(count==10):
##        pass
##    else:
##        rec_num(b)
##rec_num(b)
