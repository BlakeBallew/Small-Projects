#Author: Blake Ballew
#Takes as input a string of letters and prints out a list from
#greatest in length to smallest of the words that can be 
#constructed from the inputted letters
#run the code via the command line
#ex. for all words made from "abcdef" -> run python scrabble.py abcdef

import nltk
#you might need to include -> nltk.download('words')
import time
import sys
from nltk.corpus import words
setofwords = set(words.words())
myWords = []

def printList():
    global myWords
    ordered = sorted(myWords, key=len, reverse=True)
    token = 0
    for x in ordered:
        token += len(x)
        if (token<70):
            print(x, end=" ")
        else:
            print(x)
            token = 0

def permutations(oldLST, newLST):
    candidate = "".join(newLST)
    if (candidate in setofwords) and (len(candidate) > 3):
        if candidate not in myWords:
            myWords.append(candidate)
    if len(oldLST) > 0:
        for x in oldLST:
            oldTMP = [*oldLST]
            oldTMP.remove(x)
            newTMP = [*newLST]
            newTMP.append(x)
            permutations(oldTMP, newTMP)

def main():
    user_args = sys.argv[1]
    startTime = time.perf_counter()
    args_to_list = list(user_args)
    permutations(args_to_list, [])
    printList()
    endTime = time.perf_counter() 
    print("\nlength of ", user_args, ": ", len(user_args))
    endTime = time.perf_counter() 
    print("Execution time: ", endTime-startTime)

if __name__ == '__main__':
    main()
