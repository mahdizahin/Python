ld=int(input("Enter your load power in Watt : "))

hr=int(input("How Much time it will run in Hours : "))

tkwr=(ld*hr)/1000

up=int(input("Whar is unit price : "))
print("Per day cost " ,tkwr*up)

print("Per month cost " ,tkwr*up*30)