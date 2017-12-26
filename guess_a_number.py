#computer will randomly generate a number from 0 to 20.  You will need to guess it.  If you guess too low or too high
#feeback is immediately given.  Then proceed to count the number of guesses it takes the user to get to the rigt number

import random


computer_generate= (random.randint(0, 20))
count = 0
play = True

while play is True:
    count += 1
    user_guess = int(input("Guess the number the computer generates: "))
    if user_guess > (computer_generate):
        print(computer_generate)
        print("Your guess is too high.")
    elif user_guess < (computer_generate):
        print(computer_generate)
        print("Your guess is too low")
    elif user_guess == computer_generate:
        print("Your guess is correct. You got it in ", count, " tries")
        play = False

