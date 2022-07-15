def myfun(n):
    return lambda a:a*n
obj1=myfun(12)
obj2=myfun(12)
print(obj1(10))
print(obj2(5))
