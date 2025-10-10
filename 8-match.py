name= input("what's your name? ")

'''
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''

'''
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # default
    case _:
        print("Who?")
'''

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # default
    case _:
        print("Who?")