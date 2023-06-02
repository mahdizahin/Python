r=int(input("Enter row : "))
c=int(input("Column : "))

matrix = []

for i in range(r):
    row=[]
    for j in range(c):
        #print(i ,j)

        value = int(input(f"Enter the value for element at [{i}][{j}]: "))

        row.append(value)
    matrix.append(row)

print("The entered matrix is:")
for row in matrix:
    print(row)