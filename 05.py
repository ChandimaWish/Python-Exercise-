UserName = input('Enter user Name:-')
Marks = int(input("Enter Your Marks:- "))

if(Marks >= 60):
    print(f"{UserName} You are allo to take admission in Come in to get The admission in university")
else:
    MarksCutoff=60-Marks
    print(f"Sorry You can not take admission, You need {MarksCutoff} Marks more to take admission ")    