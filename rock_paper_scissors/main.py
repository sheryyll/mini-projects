import random
from ascii_art import rock, paper, scissors 

# Store ASCII art in a list for easy access
game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0

# Main loop
while input("Do you want to play Rock, Paper, Scissors? Type 'y' or 'n': ").lower() == 'y':
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. You lose this round!")
        computer_score += 1
        continue

    # Show user choice
    print("You chose:")
    print(game_images[user_choice])

    # Computer randomly chooses
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Decide winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Score: You {user_score} - Computer {computer_score}")

# Final result
print("\nFinal Score:")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("You are the overall winner!")
elif user_score < computer_score:
    print("Computer is the overall winner!")
else:
    print("It's an overall draw!")
