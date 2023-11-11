a = int(input("Enter 1st number"))
b = int(input("Enter 1st number"))
c = (input("Insert a operator to perform"))

if(c == '+'):
    print("Addition of two number" +str(a+b))
elif (c == '-'):
    print("Subtraction two number" +str(a-b))
elif (c == '*'):
    print("Multification two number" +str(a*b))    
elif (c == '%'):
    print("mod oftwo number" +str(a%b))   
elif (c == '/'):
    print("Division two number" +str(a/b))     
else:
    print("Incalid Operator Please Enter correct Operator")    


