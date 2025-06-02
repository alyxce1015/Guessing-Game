import random

"""
Print wrong guesses
track attempts
print leters that are guessed correctly
print correct guesses
prompt to guess a letter 
maybe use list/hash map to keep track of already guessed letters so no repeats
"""

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']



def guessing_game(): 
    # chooses random word from bank
    word = random.choice(word_bank)
    attempts = 10
    # creates word as a blank
    word_to_guess = ['_'] * len(word)

    # word display
    while attempts > 0:
        print("Current word: " + ' '.join(word_to_guess))
        user_guess = input("Guess a letter: ")

        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    word_to_guess[i] = user_guess
            print()
            print("Nice Guess!")
           
        else:
            attempts -= 1
            print("wrong guess try again.")
            print("Attempts remaining: " + str(attempts))
            print()

        if '_' not in word_to_guess:
            print()
            print("You guessed the word correctly nice job!")
            break



guessing_game()