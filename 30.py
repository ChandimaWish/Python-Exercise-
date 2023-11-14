x = int(input("Enter A Number"))
y = int(input("Enter B Number"))

def max(a,b):
  
    print("THis result is coming from the function")
    print(f"a={a}")
    print(f"b={b}")
    if(a>b):
        print(" A is greater")
    else:
        print("B is greater")

max(x,y)    