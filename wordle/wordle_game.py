#Author: Blake Ballew
#Description: lets user play wordle game with option of displaying hints
import pool
import sys


#parameters: none
#returns: desired number of letters to be used in wordle word
def welcome():
    print("\nWelcome to wordle! Here are the instructions:")
    print("You will recieve N attempts to guess an N letter word.")
    letters = int(input("How many letters would you like in your 'mystery' word? The wordle default is 5. \n"))
    print("Once you enter a guess, it will be returned accoring to the following:")
    print("[] surrounding one or more letters indicates those letters are in the word and in the correct locations.")
    print("() surrounding any given letter indicates that letter is in the word, but not placed correctly.")
    print("Any letters not enclosed by [] or () are not letters of the word.")
    print("Lastly, to recieve a list of possible words at any time, enter the string 'show'.")
    print(f"Now without further ado, please enter your opening {letters} letter word!")
    return letters

#parameters: guess is user guess, word is wordle word, N is as chosen in welcome() function
#returns: string and list form of user guess according to wordle rules
def format_result(guess, word, N):
    formatted = list(guess)

    dictionary = {}

    for x in range(N):
        dictionary.update({guess[x]: word.count(guess[x])})

    for x in range(N):
        current = guess[x]
        if current == word[x]:
            formatted[x] = "["+current+"]"
            dictionary[current] -= 1

    for x in range(N):
        current = guess[x]
        if (current in word) and (dictionary[current] > 0) and (formatted[x][0] != "["):
            formatted[x] = "("+current+")"
            dictionary[current] -= 1

    return "".join(formatted), formatted

#main function where user plays the wordle game
def main():
    attempts = welcome()
    N = attempts
    wordpool = pool.create(N)
    word = wordpool[0]
    wordpool.sort()
    wordpool.insert(0, "default")
    while attempts > 0:
        guess = str(input())
        
        #overlays result ontop of user input via adaptation of solution from
        #https://stackoverflow.com/questions/30354252/how-to-avoid-line-break-after-user-input-in-python
        CURSOR_UP_ONE = '\x1b[1A' 
        ERASE_LINE = '\x1b[2K'
        if guess != "show":
            if len(guess) == N:
                if pool.contains(guess):
                    result = format_result(guess, word, N)
                    print(CURSOR_UP_ONE + ERASE_LINE + pool.p_formatted(result[0]))
                    if guess == word:
                        print("You found the word! Good job :)")
                        print(f"Guesses: {N-attempts+1}")
                        sys.exit()
                    pool.update(result[1], guess, wordpool)
                    attempts -= 1
                else:
                    print("Error: word not found in nltk word set")
            else:
                print("Error: word does not have proper length")
        else:
            pool.p_candidates(wordpool)
    print("Sorry, you ran out of guesses :(")
    print(f"The word was: {word}")

if __name__ == "__main__":
    main()