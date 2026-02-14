
"""
x = int(input("what is x? "))
y = int(input("what is y? "))

print(x+y)

"""
x = float(input("what is x? "))
y = float(input("what is y? "))


#to nearest integer
z = (x + y)
print(z)
print(f"{z:,}")


#round to nearest digit at given position
z = round(x/y,3)
#another approach to round at second digit...if we avoid roud function..2f
#print(f"{z:.2f}")
print(z)