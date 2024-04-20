import random

# the upper bound of the range only includes every number up to it but not the number itself.  range(1, 11) will include all numbers between 1 and 10.
r = range(1, 11)


def get_user_choice():
    while True:
        # inputs are always treated as strings in python, so we need to convert the input to an integer here
        user_choice = int(input("Select a number between 1 and 10: "))
        if user_choice in r:
            return user_choice
        else:
            print("Invalid selection. You must select a number between 1 and 10")


def get_computer_choice():
    return random.randint(1, 10)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print("Welcome to the number guessing game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("The number was " + str(computer_choice))
    print(determine_winner(user_choice, computer_choice))

    if play_again():
        play_game()
    else:
        print("Thanks for playing!")


def play_again():
    choice = input("Play again? (Y or N) ").upper()
    return choice == "Y"  # evaluates whether the user's input is "Y". If the input is "Y", this expression evaluates to True or False

# returning back to line 35
# If play_again() returns True (which happens if the user entered "Y"), the condition in the if statement is true, and play_game() calls itself. This is a recursive call, essentially starting the game over again.
# If play_again() returns False (which happens if the user entered anything other than "Y"), the else block executes, printing "Thanks for playing!" and the function completes without calling play_game() again, thus ending the loop.


# Start the game
play_game()
