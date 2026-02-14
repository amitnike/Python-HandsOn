# Ask user for his name
name = input("Please enter your name -:").strip().title()

"""
multi line comment
"""

firstname,lastname = name.split(" ")
print(f"Hello {firstname}, welcome to python programming")

#merge the code into single line
#name = input("Please enter your name -:").capitalize().title()

"""
#remove whitespaces
name = name.strip()
#convert to capitals
name = name.capitalize()
#convert to title
name = name.title()

# do it together
name = name.strip().title()

# print the user name
# string concatenation
print("hello to world by "+ name)
#number of arguments passed to print function
print("hello to world by",name)

#print(*objects, sep=' ', end='\n')
print("hello to world by ",end="")
print(name)

print("hello to world by ",name,sep="???")
# can use " " as well as ' '
print('hello to world by ',name,sep='???')

#use of escape chars
print("hello \"friend\"")

#use of  f..to format the string in special way
print(f"hello to world by,{name}")
"""



