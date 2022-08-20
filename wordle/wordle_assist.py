#Author: Blake Ballew
#Description: allows user to deduce wordle word

import pool

#prints welcome message
def welcome():
    print("\nTo deduce your wordle word, please enter your guesses in the following format:")
    print("Put all guesses that are in the correct place (green) in brackets []")
    print("Put all guesses that are in the word, but incorrect place (yellow) in parentheses ()")
    print("Leave any letters not found in the word (grey) as they were before")
    print("Here's an example input :")
    print("Your guess was 'hello', but only 'h' and 'e' were in the correct locations, while 'l' was in the word but misplaced")
    print("You would then input [h][e](l)lo OR [h][e]l(l)o")
    print("Once your word has been deduced or you would like to exit, type 'end'\n")
    print("Please enter your first input")

#converts input from word to list for processing 
def convert_wl(guess):
    guess = list(guess)
    output = []
    x = 0
    while x < len(guess):
        if (guess[x] == "[") or (guess[x] == "("):
            output.append("".join(guess[x:x+3]))
            del guess[x]
            del guess[x]
            del guess[x]
        else:
            output.append(guess[x])
            x += 1
    return output

#strips input from all () and []
def convert_fw(guess):
    output = ""
    for char in guess:
        if char.isalpha():
            output += char
    return output

def main():
    welcome()
    wordpool = pool.create(5)
    wordpool.sort()
    wordpool.insert(0, "word not found in nltk")
    for attempt in range(5):
        guess = str(input())
        if guess == "end":
            break
        elif guess == "show":
            pool.p_candidates(wordpool)
        else:
            if len(guess) >=5:
                listguess = convert_wl(guess)
                word = convert_fw(guess)
                pool.update(listguess, word, wordpool)
                print("pool updated... type 'show' to see")
            else:
                print("Error: word must be of length 10")

if __name__ == "__main__":
    main()