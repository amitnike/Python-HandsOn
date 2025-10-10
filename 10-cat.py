def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        n = int(input("Number: "))
        if n > 0:
            break
    return n
        

def meow(n):
    for _ in range(n):
        print("Meow")

main()
