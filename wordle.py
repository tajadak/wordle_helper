#!/usr/bin/env python3

'''
A helper to solve Wordle games in action!
Narrows down word list using a json containing guess feedback information.

Author: Tony Audi teavse@rit.edu
'''
import ast

ASSETS_PATH = '/assets'
POSSIBLE_ANSWERS_PATH = f'.{ASSETS_PATH}/wordle-allowed-guesses.txt'
WORDS = sorted([word.strip() for word in open(POSSIBLE_ANSWERS_PATH).readlines()]) # Possible answers
CONDITIONS_PATH = f'.{ASSETS_PATH}/conditions.json'

with open(CONDITIONS_PATH) as f:
    data = f.read()
CONDITIONS = ast.literal_eval(data)

# print(CONDITIONS)

included_letters = ''
for pos in 'abcde':
    included_letters += CONDITIONS[pos].lower()

# Remove any words that don't include the letters we know are good
NEW_WORDS = list()
for word in WORDS:
    keep = True
    # for mustContain in CONDITIONS['Included']:
    for mustContain in included_letters:
        if mustContain not in word:
            keep = False
    if keep:
        NEW_WORDS.append(word)
WORDS = NEW_WORDS

# Remove any words that include letters we know are not good
NEW_WORDS = list()
for word in WORDS:
    keep = True
    for mustExclude in CONDITIONS['Excluded'].lower():
        if mustExclude in word:
            keep = False
    if keep:
        NEW_WORDS.append(word)
WORDS = NEW_WORDS

# Remove any words that don't have the good letters in the correct positions
for pos in '12345':
    NEW_WORDS = list()
    for word in WORDS:
        mustMatch = CONDITIONS[pos].lower()
        if mustMatch == '' or word[int(pos) - 1] == mustMatch:
            NEW_WORDS.append(word)
    WORDS = NEW_WORDS

# Remove any words that have the good letters in the wrong positions
i = -1
for pos in 'abcde':
    i += 1
    NEW_WORDS = list()
    for word in WORDS:
        mustExclude = CONDITIONS[pos].lower()
        if len(mustExclude) == 0:
            NEW_WORDS.append(word)
        else:
            keep = True
            for keepOut in mustExclude:
                if word[int(i)] == keepOut:
                    keep = False
            if keep and word not in NEW_WORDS:
                NEW_WORDS.append(word)
    WORDS = NEW_WORDS

# print(WORDS)
for starter in 'abcdefghijklmnopqrstuvwxyz':
    for word in WORDS:
        if word[0] == starter:
            print(word, end = ' ')
    print()
print()
print(len(WORDS))
