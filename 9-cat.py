'''
i = 3

while i != 0:
    print("Meow")
    i = i-1
'''
i = 0

while i < 3:
    print("Meow")
    # i = i+1
    i += 1

for i in [0,1,2]:
    print("Meow in for loop")

for i in range(3):
    print("Meow in for range loop")

print ("Meow By Multiply by 3\n" *3, end="")