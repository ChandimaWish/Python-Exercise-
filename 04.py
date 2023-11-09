UserName = input('Enter user Name:-')
Age = int(input("Enter Your Age In The System :-"))


if(Age >= 18):
    print(f"Hi {UserName}! You can take the participate")
else:
    waitingYear= 18-Age
    print(f"Sorry! You cannot participate in voting You will be able to participate after {waitingYear} year")
