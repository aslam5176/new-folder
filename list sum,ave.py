##TO CHECK SUM(+) AND AVERAGE(/)
a=[2,4,9,7,9,2,67,98]
b=0
for i in a:
    b+=i
    print(i)    
c=b/len(a)
print("sum =",b)
print("average= ",c)

##TO CHECK MAXIMUM NUMBER USING FUNCTION AND CONDION
a=input("enter the number")
b=input("enter the number")
c=input("enter the number")
def maxnum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
print(maxnum(a,b,c))    
##TO USING MAX METHOD MAX NUMBERS
a=input("enter the number")
b=input("enter the number")
c=input("enter the number")
maximum=max(a,b,c)
print(maximum)


5
