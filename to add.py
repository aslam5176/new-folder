 ##def add(a):
##    return a+a
##numbers=[1,2,3,4,5]
##c=map(add,numbers)
##print(list(c))

##a=[1,2,3,4,5]
##for i in range(len(a)):
####    a[i]=a[i]+a[i]
##print(a)    

####TO CHECK MAXIMUM OF TWO NUMBERS USINF MAX KEYWORD
##a=10
##b=20
##c=max(a,b)
##print(c)

##a=-1
##b=-4
##c=max(a,b)
##print(c)
####DON'T USING MAX KEYWORD
##
##def max_numbers(a,b,c):
##        
##    if a>b and a>c:
##        return a
##    elif b>c: 
##        return b
##    else:
##        return c
##
##a=8
##b=20
##c=10
##
##print(max_numbers(a,b,c))
####TO CHECK MINIMUM OF NUMBERS USING 'MIN' KEYWORD
a=10
b=29
c=30
h=min(a,b,c)
print(h)

####TO CHECK MINIMUM OF NUMBERS WITHOUT KEYWORD
def min_numbers(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c
a=10
b=20
c=30
print(min_numbers(a,b,c))



    



    






