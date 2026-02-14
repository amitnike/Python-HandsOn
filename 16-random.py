import random
#from random import choice
#if we imported specific functions from the random module, we can use them directly without the random. prefix.
coin = random.choice(["heads","tails"])
# choice is a function that can be used to select a random element from a list.
print(coin)
# randint is a function that can be used to generate a random integer between two values.
number = random.randint(1,12)
print(number)

cards = ["queen","king","jack"]
#shuffle is a function that can be used to shuffle a list in place.
random.shuffle(cards)
for card in cards:
    print(card)