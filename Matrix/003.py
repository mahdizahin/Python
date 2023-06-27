
xr=int(input("Enter row : "))
xc=int(input("Enter Column : "))

matrix = []

for i in range(xr):
    row=[]
    for j in range(xc):
        #print(i ,j)

        value = int(input(f"Enter the value for element at [{i}][{j}]: "))

        row.append(value)
    matrix.append(row)

print("The entered matrix is:")
for row in matrix:
    print(row)