###dice rolling easy level project
import random
while True:
    user = input("roll the dice (y/n): ")
    if user == "y" or user == "Y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif user == "n" or user == "N":
        print("thank you for coming")
        break
    else :
        print("invalid choice")

