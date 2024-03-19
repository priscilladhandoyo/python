import random

words = ['python', 'java', 'kolin', 'javascript', 'ruby', 'swift']

#randomly choose a word from the list
chosen_word = random.choice(words)

#create a list of underscores which equal to the length of chosen_word
word_display = ['_' for _ in chosen_word]

#number of allowed attempts
attempts = 8 

print("Welcome to Hangman!")

#semi infinite while loop
#until the all the "_" have a alphabets in it or
#until they run out of attempts
while attempts > 0 and '_' in word_display:

    #take an empty string and we concatenate it with every element of the word display
    print("\n" + ' '.join(word_display)) 
    guess = input("Guess a letter: ").lower()

    #check if the guess letters are in the chosen_word
    if guess in chosen_word:

        #for ex: python, index = 0, letter = p
        for index, letter in enumerate(chosen_word):
            if letter == guess:

                #reveal the letter
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word, idiot !!!")
        attempts -= 1

#game conclusion
if '_' not in word_display:
    print("You huessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")