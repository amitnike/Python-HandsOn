def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#ensure main is invoked from its own class
if __name__ == "__main__":
    main()