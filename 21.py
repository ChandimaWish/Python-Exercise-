import array

def largest(array,n):
    mx = array[0]

    for i in range(1,n):
        if array[i] > mx:
            mx = array[i]
    return mx        


Num1=int(input('Enter First Number'))

Num2=int(input('Enter Second Number'))

Num3=int(input('Enter Third Number'))

Num4=int(input('Enter fourth Number'))

Numg=int(input('Enter fifth Number'))

array=[Num1,Num2,Num3,Num4,Numg]
n = len(array)

ans= largest(array,n)
print(array)
print("Largest i  given array is ", ans)




