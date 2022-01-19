import os 
import random 
from typing import Dict, List

os.system("") # makes colours work

COLOUR = {
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "WHITE": "\033[89m",
    "ENDC": "\033[0m",
}

def load_words() -> List[str]:
    with open('dictionary.txt', 'r') as f:
        lines = f.readlines()
    return [w.strip() for w in lines if len(w.strip()) == 5]

def count_occurances(word: str) -> Dict[str, int]:
    occurances = dict()
    for i in range(len(word)):
        if word[i] not in occurances:occurances[word[i]] = 1
        else:occurances[word[i]] += 1
    return occurances

def check_input(uin: str, target: str) -> None:
    target_occurances = count_occurances(target)
    exact = dict()
    for i in range(len(uin)):
        if uin[i] not in exact:
            exact[uin[i]] = 0
        if uin[i] == target[i]:
            exact[uin[i]] += 1
    compared = dict()
    print_list = []
    for i in range(len(uin)):
        if uin[i] not in compared:
            compared[uin[i]] = 0
        if uin[i] == target[i]:
            print_list.append(COLOUR["ENDC"]+COLOUR['GREEN'])
        elif uin[i] in target and compared[uin[i]] < target_occurances[uin[i]] and exact[uin[i]] < target_occurances[uin[i]]:
            print_list.append(COLOUR["ENDC"]+COLOUR['YELLOW'])
        else:
            print_list.append(COLOUR["ENDC"]+COLOUR['WHITE'])
        print_list.append(uin[i])
        compared[uin[i]] += 1
    print_list.append(COLOUR["ENDC"])
    print(*print_list, sep="")

def main():
    words = load_words()
    target = random.choice(words)
    print("Type your guess and press 'enter':")
    for i in range(5):
        uin = ""
        while len(uin) != 5 and uin not in words:
            uin = input().upper()
            if len(uin)!=5:
                print("Please use 5 characters")
            elif uin not in words:
                print("Please use a valid word")
                uin = ''
        print(f"Guess {i+1} of 5:")
        check_input(uin, target)
        if uin == target:
            print("Correct!")
            return
    print(f"All Guesses used. The word was {target}")


if __name__ == '__main__':
    main()