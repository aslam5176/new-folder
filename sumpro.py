a=[12,14,15,108]
r=0



for i in a:
    print(i)
    sum=0
    product=1
    v=i
    while(v>0):
        lnum=v%10
        sum+=lnum
        if(lnum != 0):
            product*=lnum
        v//=10    
        print('sum',sum)
        print('product',product, "\n")    
    if(i%sum ==0 and i %product==0):
        print("divisible")
           r+=1
    else:
        print("not divisble")

print(r)
