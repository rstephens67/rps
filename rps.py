from starters import choice

def compare(choice1, choice2):
    """Input "Rock", "Paper", or "Scissors" for choice1 and choice2 to play a game of Rock, Paper, Scissors."""
    if choice1 == choice2:
        print("Draw!")
    elif choice1 == 'rock':
        if choice2 == 'paper':
            print("Paper covers rock! If that makes any sense!?")
        elif choice2 == 'scissors':
            print("Rock wins, that ROCKS LOLOLOL!!!1111!")
    elif choice1 == 'paper':
        if choice2 == 'rock':
            print("Paper cover rock! If that makes any sense!?")
        elif choice2 == 'scissors':
            print("Scissors cuts paper! TAKE THAT")
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            print("Rock wins, that ROCKS LOLOLOL!!!1111!")
        elif choice2 == 'paper':
            print("Scissors cuts paper! TAKE THAT")
    else:
        print("That's not good enough, try again")

rounds = int(raw_input("Enter number of rounds: "))
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
