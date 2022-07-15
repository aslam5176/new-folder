a=[12,14,28,104,2]
l = str(a)
r = []

for i in a:
    print(i)
    sum = 0
    for j in str(i):
        sum+=int(j)
    r.append(sum)
print("a =",a)    
print("value of sum",r)
product=0
for i in a:
    product+=i
print(product)
##a=int(input("enter the number"))
##
##
####a=[12,17,19]
##sum=0
##product=1
##b=a
##while(b>0):  
##    lnum=b%10
##    sum+=lnum
##    b//=10
##    
##    if(lnum!=0):
##        product*=lnum
##    else:
##        pass
##
##   
##print(sum,"sum")
##print(product,"product")   
##
##
##if(a%sum==0):
##    print(1)
##else:
##    print(0)
