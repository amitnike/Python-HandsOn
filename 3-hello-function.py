# create main function to call the hello
def main():
  hello()
  name = input("Please enter your name -:")
  hello(name)

# define a fuction + set default value to parameter
def hello(to="there"):
    print(f"Hello {to}, welcome to python programming")

#invoke main ...when i ran .py class
main()