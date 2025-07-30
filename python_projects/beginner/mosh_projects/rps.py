### rock paper scissor game basic
import random


choices = ('r', 'p', 's')
while True:
    user_choice = input("choose the rock, paper, scissor (r, p, s) :-- ").lower()
    if user_choice not in choices:
        print("invalid choice")
    computer_choice = random.choice(choices)
    print(f'your choice {user_choice}')
    print(f'bot choice {computer_choice}')
    if user_choice == computer_choice:
        print("tie")
    elif user_choice == "r" and computer_choice == "s":
        print("you win")
    elif user_choice == "r" and computer_choice == "p":
        print("you lose")
    elif user_choice == "p" and computer_choice == "s":
        print("you lose")
    elif user_choice == "p" and computer_choice == "r":
        print("you win")
    elif user_choice == "s" and computer_choice == "r":
        print("you lose")
    elif user_choice == "s" and computer_choice == "p":
        print("you win")
    else:
        print("invalid choice")
    
    play_again = input("want to play again (y/n):-- ").lower()
    if play_again == "n":
        break


