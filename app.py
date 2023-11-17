

#If the user input is yes, call a function called playgame. If the user input is no, show a message saying goodbye.
def playgame():
    user_input = input("Choose one of the following options: rock, paper, scissors: ")
    while user_input != "rock" and user_input != "paper" and user_input != "scissors":
        print("Error, please choose a valid option")
        user_input = input("Choose one of the following options: rock, paper, scissors: ")
    import random
    computer_input = random.randint(0,2)
    if computer_input == 0:
        computer_input = "rock"
    elif computer_input == 1:
        computer_input = "paper"
    else:
        computer_input = "scissors"
    print("You chose " + user_input)
    print("The computer chose " + computer_input)
    if user_input == computer_input:
        print("It's a tie!")    
    elif user_input == "rock" and computer_input == "scissors":
        print("You won!")
    elif user_input == "scissors" and computer_input == "paper":
        print("You won!")
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
    else:
        print("The computer won!")
    play_again = input("Do you want to play again? ")
    while play_again != "yes" and play_again != "no":
        print("Error, please choose a valid option")
        play_again = input("Do you want to play again? ")
    if play_again == "yes":
        playgame()
    else:
        print("Goodbye!")
playgame()


