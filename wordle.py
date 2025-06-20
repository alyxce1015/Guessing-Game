import random

"""
currently working on getting hints to work
i.e.
* also work on not allowing the same correct letters already in the word

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
    print(" ", len(wordlist), "words loaded.\n")

    # use this line to print word list if needed 
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

    # this is to test functionality
    print("The word is", word)


    # chooses random word from bank
    attempts = 10
    # creates word as a blank
    word_to_guess = ['_'] * len(word)
    guessedLetters = list()
    # word display
    while attempts > 0:
        
        print("Letters guessed:", ", ".join(guessedLetters))
        print("Current word: " + ' '.join(word_to_guess))
        user_guess = input("Guess a letter: ")
        print()

        # makes sure there is no multiple letters in guess
        if len(user_guess) > 1:
            print("Error: guess must be 1 letter only. Please restart")
            break

        if user_guess in word:
            for i in range(len(word)):
                if word[i] == user_guess:
                    word_to_guess[i] = user_guess
            print("Nice Guess!")
           
        else:
            if user_guess in guessedLetters:
                print("You have already guessed:", user_guess)
                print("Attempts remaining: " + str(attempts))
                continue
            else:
                attempts -= 1
                guessedLetters.append(user_guess)
                print("Wrong guess.")
                print("Attempts remaining: " + str(attempts), '\n')

        if '_' not in word_to_guess:
            print("\nThe word was:", word)
            print("You guessed the word correctly nice job!")
            break
        elif attempts == 0:
            print("Gameover!\n")
            print("The word was: " + word)

        



guessing_game()