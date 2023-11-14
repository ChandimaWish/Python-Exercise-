MaxStart=int(input("Enter staring Number"))
MaxEND=int(input("Enter end Number"))

if(MaxStart>MaxEND):
    for i in range(MaxStart,MaxEND):
        print(i)

else:
    for i in range(MaxEND,MaxStart):
        print(i)
