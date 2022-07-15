##TO SWAP THE LIST ELEMENT
a=[1,23,56,98,6]
def swaplist(a):
    b=len(a)
    c=a[0]
    a[0]=a[b-1]
    a[b-1]=c
    return a
print(swaplist(a))

##TO SWAP THE LIST POSITION
x=[10,20,30,40,50,70]
pos1=1
pos2=6
def swap_position(x, pos1,pos2):
    x[pos1],x[pos2]=x[pos2],x[pos1]
    return x
    
print(swap_position(x,pos1-1,pos2-1))   

##TO CHECK LENGTH OF NUMBERS
a=[12,14,15,16,17]
b=0
print("the list is:" + str(a))
for i in a:
    b=b+1
    print("the length of number is:" + str(b))





        
