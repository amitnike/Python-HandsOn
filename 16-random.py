import random
#from random import choice

coin = random.choice(["heads","tails"])
#coin = choice(["heads","tails"])
print(coin)
number = random.randint(1,12)
print(number)

cards = ["queen","king","jack"]
random.shuffle(cards)
for card in cards:
    print(card)