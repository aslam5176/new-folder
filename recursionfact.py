##
##FACTORIAL USING RECURSION
##n=int(input("enter the number"))
##def factorial(n):
##    if(n==1 or n==0):
##        return 1
##    else:
##       return(n*factorial(n-1))
##       factorial(n)    
##print("factorial:",factorial(n))

####to check fibonacci series using recursion
n = int(input("enter the number "))  
def fibonacci(n): 
   if n <= 1:  
       return n   
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))
print("the Fibonacci sequence is:")
for i in range(n):
    print(fibonacci(i))
