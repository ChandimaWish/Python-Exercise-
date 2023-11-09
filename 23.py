Letter = input('Enter Charter')
if(Letter == 'a','e','i','o','u'):
    print("It is a vowel")
# if (Letter == 'a','A'):
#     print("It is a vowel")
# elif(Letter == 'e','E'):
#     print("It is a vowel")
# elif(Letter == 'i','I'):
#     print("It is a vowel")
# elif(Letter == 'o','O'):
#     print("It is a vowel")

elif Letter.isnumeric():
    print("It is a number")
else:
    print("It is a Constant")
        
