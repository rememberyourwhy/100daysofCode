#This function will return if each character in a_word match (user_input with a random picked word ("a word")) from a list

#Store words in a list
#use random to pick one from that list "word"

#get input from user ("guess_character") to guess (type = "char")
#iterate through every character of "word" and return if "word_element" == "char"
import random
import hangman_words
import hangman_art
def check_guessed_char(word, guess_character):
    for element in word:
        if element == guess_character:
            print(True)
        else:
            print(False)

def replacing_blank_spaces(word, guess_character, word_blank):
    for index in range(len(word)):
        if word[index] == guess_character:
            word_blank[index] = guess_character
    return word_blank




#Start the game
def main_game():
    # Auto generate part
    print("Welcome to Hangman game")
    logo = hangman_art.logo
    print(logo)
    # Create a list of word and use random to get one of them
    list_word = hangman_words.word_list
    word = list_word[random.randint(0, len(list_word) - 1)]
    # Now generate a blank word that represent "word", then print.
    word_blank = ["_" for element in word]
    print(word_blank)
    stages = hangman_art.stages
    lives = 6
    while "_" in word_blank and lives > 0:

        #User Input part
        #Ask user which character to guess
        guess_character = input("Guess a character ")

        #Processing and print output
        #Run check
        #check_guessed_char(word, guess_character)
        word_blank_pre = list(word_blank)
        word_blank = replacing_blank_spaces(word, guess_character, word_blank)
        if word_blank != word_blank_pre:
            print(word_blank)
        else:
            lives -= 1
            print(stages[lives])
    result = lives > 0
    if result:
        print("You won")
    else:
        print(f"The word is {word}")
        print("You lost")


result = main_game()
