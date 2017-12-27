import random

coin = ['tails', 'heads']

while True:
    x = input("Would you like for the computer to flip the coin for you?  Type Yes in any version to continue. ")
    x = x.lower()
    if x == 'yes' or x == 'Yes' or x == "YES" or x == "y" or x == "ye":
        cointoss = coin[random.randint(0, 1)]
        print("And the results are.....  ", cointoss)
    else:
        print('Thanks for playing!')
        exit()
