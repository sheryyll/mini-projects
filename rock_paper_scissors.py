import random

print("==================================")
print(" Rock Paper Scissors Lizard Spock")
print("==================================")

print("1 is for '✊' (Rock)")
print("2 is for '✋' (Paper)")
print("3 is for '✌️' (Scissors)")
print("4 is for '🦎' (Lizard)")
print("5 is for '🖖' (Spock)")

next_game = "yes"
while next_game == "yes":
    player = int(input("Pick a number (1-5): "))
    computer = random.randint(1,5)

    if player == 1:
        print("You chose : ✊")
    elif player == 2:
        print("You chose : ✋")
    elif player == 3:
        print("You chose : ✌️")
    elif player == 4:
        print("You chose : 🦎")
    elif player == 5:
        print("You chose : 🖖")
    else:
        print("Invalid choice!")
        continue

    if computer == 1:
        print("CPU chose : ✊")
    elif computer == 2:
        print("CPU chose : ✋")
    elif computer == 3:
        print("CPU chose : ✌️")
    elif computer == 4:
        print("CPU chose : 🦎")
    else:
        print("CPU chose : 🖖")

    if player == computer:
        print("It's a tie!")
    elif (player == 1 and (computer == 3 or computer == 4)) \
      or (player == 2 and (computer == 1 or computer == 5)) \
      or (player == 3 and (computer == 2 or computer == 4)) \
      or (player == 4 and (computer == 2 or computer == 5)) \
      or (player == 5 and (computer == 1 or computer == 3)):
        print("The player won!")
    else:
        print("CPU won!")

    next_game = input("Do you want to continue to play? (yes / no): ").lower()
