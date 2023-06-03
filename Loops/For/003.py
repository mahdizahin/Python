size=int(input("Enter Array Size : "))
arr = []
for i in range(size):
    value=int(input(f"Enter number at index [{i}] : "))
    arr.append(value)


for j in arr:
    print(j)