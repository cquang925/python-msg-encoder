#  this randomizes a list and assigns values to items in a dictionary and then saves to csv file

import random
import csv

alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']',
           "\\", ';', '\'', ',', '.', '/', '{', '}', '|', ':', '"', '<', '>', '?']

alphaNumSym = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~',
               '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', "\\", ';', '\'',
               ',', '.', '/', '{', '}', '|', ':', '"', '<', '>', '?', ' ']

characters = {}


def randomize():
    random.shuffle(alphaNumSym)
    val = 1

    for char in alphaNumSym:
        characters[char] = val
        val = val + 1


def save_key():
    master_key = csv.writer(open('key.csv', 'w', newline=''))
    for key, val in characters.items():
        master_key.writerow([key, val])


def import_key():
    master_key = open('key.csv', 'r')
    reader = csv.reader(master_key)

    for row in reader:
        characters[row[0]] = row[1]


def view_key():
    print(characters)