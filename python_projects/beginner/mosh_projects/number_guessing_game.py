### number guessing game

import random
guess_number = random.randint(1, 100)
while True:
    try:
        user_input = int(input("guess the number : "))
        
        if user_input < guess_number:
            print("too low")
        elif user_input > guess_number:
            print("too high")
        else:
            print("you won")
            break
    except ValueError:
        print("please enter valid number")
