#Author: Blake Ballew
#Description: Finds allocation of X items among Y people given each person's top Z items such that,
#as a whole, the group is the "happiest"
import random
import sys
import time

def create_test(num_people, num_choices, num_picks):
    total_choices = []
    total_people = []
    
    for x in range(1, num_people+1):
        person = "person"+str(x)
        total_people.append(person)
        choices = []
        for y in range(1, num_choices+1):
            current = "thing"+str(y)
            choices.append(current)
        random.shuffle(choices)
        temp = [*choices]
        total_choices.append(temp[:num_picks])
    return [total_people, total_choices]

def print_info(people, things, num_picks):
    for i in range(len(people)):
        print(people[i], end=": ")
        for j in range(num_picks-1):
            print(things[i][j], end= " ->  ") 
        print(things[i][num_picks-1])

def best(num_people, people, things):
    candidates = []

    def allocate(col, taken, sum, dictionary):
        if col == num_people:
            candidates.append([sum, dictionary])
        else:
            for i in range(len(things[0])):
                current = things[col][i]
                if current not in taken:
                    temp_col = col
                    temp_taken = taken.copy()
                    temp_sum = sum
                    temp_dictionary = dictionary.copy()
                    
                    temp_col += 1
                    temp_taken.append(current)
                    temp_sum += i**3
                    temp_dictionary.update({people[col]: current})

                    allocate(temp_col, temp_taken, temp_sum, temp_dictionary)
    
    allocate(0, [], 0, {})

    best = ["inf", {"no feasible allocation": "-1"}]
    min_sum = num_people**5
    for cand in candidates:
        if cand[0] < min_sum:
            min_sum = cand[0]
            best = cand.copy()

    return [len(candidates), best[0], best[1]]

def collect_data():
    total_people = []
    total_choices = []

    print("Please enter the data in the following format: ")
    print("'name 1' 'first pick' 'second pick' ... 'nth pick'")
    print("'name 2' 'first pick' 'second pick' ... 'nth pick'")
    print("   .            .                           .     ")
    print("   .                        .               .     ")
    print("   .                                        .     ")
    print("'name n' 'first pick' 'second pick' ... 'nth pick'")
    print("Noting that each entry per row is separated by a space")
    print("Once you are finished, type 'end'\n")
    while True:
        inp = str(input())
        if inp == "end":
            break
        info = inp.split(" ")
        total_people.append(info[0])
        total_choices.append(info[1:])
    print()
    return [total_people, total_choices]

def main():
    choice = str(input("Would you like to enter data or generate test cases? (d or t) "))
    if choice == "d":
        data = collect_data()
        people = data[0]
        things = data[1]  
        num_picks = len(things[1])
        num_people = len(data[0])

    elif choice == "t":
        num_people = int(input("Enter # people  "))
        num_choices = int(input("Enter # choices "))
        num_picks = int(input("Enter # picks   "))
        test_case = create_test(num_people, num_choices, num_picks)
        people = test_case[0]
        things = test_case[1]
    else:
        print("Error: input not valid")
        sys.exit()
    startTime = time.perf_counter()
    print_info(people, things, num_picks)
    results = best(num_people, people, things)
    total_candidates = results[0]    
    unhappiness = results[1]
    best_allocation = results[2]
    endTime = time.perf_counter() 
    print(f"\nExecution time: {endTime-startTime}")
    print(f"total candidates: {total_candidates}")
    print(f"minimal unhappiness found: {unhappiness}")
    for i, j in best_allocation.items():
        print(f"{i} -> {j}")

if __name__ == "__main__": 
    main()
