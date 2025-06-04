import random

"""
currently working on getting hints to work
i.e. create a list of letters that are already used to narrow down the options
"""



"""Function to load words into a list that is readable in program"""
def load_words(words):
    print("loading word list from file...")
    wordlist = list()
    # open words file to read
    with open(words) as f:
        # read each line one by one 
        for line in f:
            # strip newline then append to list
            wordlist.append(line.rstrip())
    print(" ", len(wordlist), "words loaded.")
    print()
    # print('\n'.join(wordlist))
    return wordlist 


# function to grab random word from word list
def choose_word_from_list(wordlist):
    return random.choice(wordlist)
# call load_words to read from words.txt 
wordlist = load_words('words.txt')




"""Function of actual game"""
def guessing_game(): 
    word = choose_word_from_list(wordlist)
    print("The word is", word)
    # chooses random word from bank
    attempts = 10
    # creates word as a blank
    word_to_guess = ['_'] * len(word)
    guessedLetters = list()
    # word display
    while attempts > 0:
        
        print(guessedLetters)
        print("Current word: " + ' '.join(word_to_guess))
        user_guess = input("Guess a letter: ")
        print()

        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    word_to_guess[i] = user_guess
            print("Nice Guess!")
           
        else:
            attempts -= 1
            guessedLetters.append(user_guess)
            print("Wrong guess try again.")
            print("Attempts remaining: " + str(attempts))
            print()

        if '_' not in word_to_guess:
            print()
            print("You guessed the word correctly nice job!")
            break
        elif attempts == 0:
            print("Gameover!\n")
            print("The word was: " + word)

        



guessing_game()