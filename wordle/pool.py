#Author: Blake Ballew
#Description: manages the functions associated with the wordle pool of valid candidates
import nltk
#might need to include -> nltk.download('words')
from nltk.corpus import words
setofwords = set(words.words())
import random


#creates pool

#parameters: N represents length of wordle word (standard wordle is 5)
#returns: pool containing only words of desired length
def create(N):
    pool = []
    for word in setofwords:
        if (len(word) == N) and word[0].islower():
            pool.append(word)
    random.shuffle(pool)
    return pool

#functions associated with updating the pool

#parameters: list_guess is list form of formatted result, word_guess is string form, and pool is current pool
#returns: updated pool
def update(list_guess, word_guess, pool):
    cand = 1
    while cand < len(pool):
        current = pool[cand]
        if not (check_1(word_guess, list_guess, current) and check_2(word_guess, list_guess, current)):
            del pool[cand]
        else:
            cand += 1

#performs necessary deductions of word pool
#returns: boolean of whether or not conditions are met 
def check_1(word_guess, list_guess, candidate):
    group_1 = []
    group_2 = []
    for letter in list_guess:
        if letter[0].isalpha():
            group_2.append(letter[0])
        else:
            group_1.append(letter[1])

    for char in group_1:
        if char in group_2:
            if group_1.count(char) != candidate.count(char):
                return False
        else:
            if word_guess.count(char) > candidate.count(char):
                return False

    for char in group_1:
        for occ in range(group_2.count(char)):
            group_2.remove(char)

    for char in group_2:
        if candidate.count(char) != 0:
            return False

    return True

#performs deductions 
#returns: boolean of whether or not conditions are met
def check_2(word_guess, list_guess, candidate):
    counter = 0
    for letter in list_guess:
        if letter[0] == "[":
            if candidate[counter] != word_guess[counter]:
                return False
        elif letter[0] == "(":
            if candidate[counter] == word_guess[counter]:
                return False
        counter += 1
    return True

#functions associated with printing the word pool

#parameters: pool is current word pool
#returns: none, instead prints candidate words from the word pool
def p_candidates(pool):
    l = len(pool)
    print("  ", end="")
    for x in range(1, l):
        print(pool[x], end=" ")
        if x%10 == 0:
            print("\n", end="  ")
    print(f"\n  Best guess: {pool[l//2]}")
    print(f"  total words: {l-1}")

#parameters: formatted is string representing formatted result -> e[xa]m(p)l(e)
#returns: pool to desired format -> [e][x][a]mp[l][e] prints as [exa]mp[le]
def p_formatted(formatted):
    x = 0
    formatted = list(formatted)
    while(x<len(formatted)-1):
        if (formatted[x] == "]") and (formatted[x+1] == "["):
            del formatted[x]
            del formatted[x]
        else:
            x += 1
    return "".join(formatted)

#returns true if guess is in nltk word set, false otherwise
def contains(guess):
    return guess in setofwords
