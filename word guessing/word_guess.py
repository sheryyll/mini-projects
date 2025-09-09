import random

#word bank
word_bank = [
    "lantern", "whisper", "orbit", "meadow", "ember",
    "quartz", "horizon", "breeze", "pixel", "canyon",
    "velvet", "thunder", "prism", "echo", "spiral",
    "shadow", "crystal", "ember", "solstice", "wave",
    "flame", "fog", "stone", "glimmer", "dream"
]

#randomly select a word from the word bank
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input("Guess a letter: ").lower()
  
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print(f'Wrong guess! Attempts left: {attempts}')
    
    if '_'  not in guessedWord:
        print(f'Congratulations! You guessed the word: {word}')
        break
else:
    if attempts == 0 and '_' in guessedWord:
        print(f'Sorry, you ran out of attempts. The word was: {word}')          
