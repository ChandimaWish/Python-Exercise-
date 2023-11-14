import array as arr
Name = input("Enter Your Name ")

a = arr.array('i',[])
for i in range(5):
    a.append(input("Enter Subject Marks"))

total = 0
for i in range(5):
    total += a[i]

print(f"Hi {Name}")
print(f"Your Marks is {i}")
print(f"See your all subject marks {total}")

