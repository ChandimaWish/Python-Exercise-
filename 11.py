Science =  int(input("Enter Your Marks In Science"))
Maths =  int(input("Enter Your Marks In Maths"))
English =  int(input("Enter Your Marks In English"))
Drama =  int(input("Enter Your Marks In Drama"))
History =  int(input("Enter Your Marks In History"))
ICT =  int(input("Enter Your Marks In ICT"))



Total =(Science+Maths+English+Drama+History+ICT)
Average = (Total/6)
percentage = int(Average*100)
print(f"Total {Total}\n Average {Average}\nPercentage{percentage}")