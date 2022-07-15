a1=input("enter the letters a1=>") 
a2=input("enter the letters a2=>")
def common_letters(a1):
    if(a1 in a2):
        return True
    else:
        False
common_letters=filter(common_letters,a1)
a2=list(common_letters)
print(a2)
