names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("what's your name? ")

# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

#better option to open and close the file
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")

#reading the file
# with open("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"hello, {line.rstrip()}")

#better option to read  the file, instead of reading+iterating lines
with open("names.txt","r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}")

#reading the file as above + do sorting in desc
with open("names.txt","r") as file:
    for line in sorted(file,reverse=True):
        print(f"hello, {line.rstrip()}")