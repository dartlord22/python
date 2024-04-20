import random
# import the random module for us to use to randomize the computers choice


def get_user_choice():
    while True:
        # convert user input to lowercase so that it will always match, assuming spelled correctly
        user_choice = input(
            "Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")


def get_computer_choice():
    # return a random selection between rock, paper, and scissors
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_rps():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chose: " + computer_choice)
    print(determine_winner(user_choice, computer_choice))


def play_again():
    choice = input("Play again? (Y or N) ").upper()
    if choice == "Y":
        return play_rps()
    else:
        print("Thanks for playing!")


# Play the game
play_rps()
play_again()
