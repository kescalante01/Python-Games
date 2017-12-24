import random

coin = ['tails', 'heads']

while True:
    x = input("Would you like to flip the coin?  Type Yes or No: ")
    x = x.lower()
    if x =='yes':
        cointoss = coin[random.randint(0, 1)]
        print(cointoss)
    else:
        print('Thanks for playing!')
        exit()