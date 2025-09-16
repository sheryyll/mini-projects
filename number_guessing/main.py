from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns  

def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        print("Invalid input. Please type 'easy' or 'hard'.")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0

    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if guess != answer and turns > 0:
            print("Guess again.")
        elif turns == 0:
            print("You've run out of guesses, you lose.")


play_game = True
while play_game:
    game()
    should_continue = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        print("Goodbye!")
        play_game = False
