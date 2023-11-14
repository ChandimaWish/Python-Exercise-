color_lst = []
for i in range(0,5,1):
    color_lst.append(input("Enter  a Color Name "))

print(f"List color name {color_lst}")
color_lst.pop()
print(f"List color name {color_lst}")
del color_lst[0]
print(f"List color name {color_lst}")