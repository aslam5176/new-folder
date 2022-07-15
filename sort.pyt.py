a=[1,5,6,9,0]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print("the second largest number is:",a[1])            
