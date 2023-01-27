import random
p_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
c_choice = random.randint(0, 2)

options = ["Rock", "Paper", "Scissors"]

# Set player choice- included basic input validation
if p_choice > 2 or p_choice < 1:
    print("Not an option try again")
elif p_choice == 0:
    print(f"You chose {options[0]}")
elif p_choice == 1:
    print(f"You chose {options[1]}")
elif p_choice == 2:
    print(f"You chose {options[2]}")

# Show computer choice
if c_choice == 0:
    print(f"The computer chose {options[0]}")
elif c_choice == 1:
    print(f"The computer chose {options[1]}")
elif c_choice == 2:
    print(f"The computer chose {options[2]}")

# Round of rock paper scissors results
if p_choice == c_choice:
    print("You draw")
elif p_choice == 1 and c_choice == 2 or p_choice == 2 and c_choice == 0 or p_choice == 0 and c_choice == 1:
    print("You lose")
else:
    print("You win")
