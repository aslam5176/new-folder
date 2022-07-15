##try:
##    f=open("demofile.txt","w")
##    try:
##        f.write("lorem ipsum")
##    except:
##        print("something went wrong")
##    finally:
##      f.close()
##except FileNotFoundError:
##    print("file not found")
##except:
##    print("something wrong")

##try:
##    print(x)
##except:
##    print("no error found")
##    
try:
    print(a)
except NameError:
    print("a is not defined")
except:
    print("something wrong")

