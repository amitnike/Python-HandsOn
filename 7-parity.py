def main():
    score= int(input("what is x? "))
    if is_even(score):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    
    '''
    if n % 2 == 0:
        return True
    else:
        return False
    '''
    
    '''
    return True if n % 2 == 0 else False
    '''

    return n % 2 == 0

main()