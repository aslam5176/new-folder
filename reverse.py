##a=int(input("enter the number"))
##b=0
##while(a>0):
##    c=a%10
##    b=b*10+c
##    a=a//10
##print(b)



a=123
b=0
while(a!=0):
    a//=10
    b+=1
print(b)
