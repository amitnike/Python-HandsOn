def main():
    x = get_int("what is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            #better to return from here using break..x will have value too
            # OR
            #return int(input("what is x? "))...no return from else is needed
        except ValueError:
            # catch the exception but do nothing
            pass
            # print just to show that input is invalid.
            # print("x is not an integer")
        else:
            #exit once input is valid or break
            return x


# raise --- to raise the exception explicity from our code
main()

