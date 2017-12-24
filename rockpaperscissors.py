import random
RPS_Wins = {
    "rock": "scissors",
    "scissors": "paper",
    "paper" : "rock"
}
RPS_choices = ("paper","scissors","rock")
computer_choice = RPS_choices[random.randint(0,2)]
print(computer_choice)
computer_choice = computer_choice.lower()
user_choice = input("Pick Paper, Rock, or Scissors")
print(user_choice)
user_choice = user_choice.lower()
if RPS_Wins[computer_choice] == user_choice:
    print("Computer Wins")
elif computer_choice == user_choice:
    print("Its a tie")
else:
    print("Computer Lost")