######LIST COMPREHENSION
##
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##newlist = []
##
##for x in fruits:
##  if "a" in x:
##    newlist.append(x)
##
##print(newlist)
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##
##newlist = [x for x in fruits if "e" in x]
##
##print(newlist)
####TO CHECK ODD OR EVEN IN LIST COMPREHENSION
a=[(i,"even")if i%2==0 else(i,"odd")for i in range(1,11)]
print(a)
