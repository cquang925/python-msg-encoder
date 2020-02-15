# created dictionary of lower case letters
lower_letters = {'a': 52, 'b': 53, 'c': 54, 'd': 55, 'e': 56, 'f': 57, 'g': 58, 'h': 59, 'i': 60, 'j': 61, 'k': 62,
                 'l': 63, 'm': 64, 'n': 65, 'o': 66, 'p': 67, 'q': 68, 'r': 69, 's': 70, 't': 71, 'u': 72, 'v': 73,
                 'w': 74, 'x': 75, 'y': 76, 'z': 77, ' ': 78}


# created definition that returns a list
def split(sentence):
    return list(sentence)


sentence = input('Write a short sentence: ')
delimit = (split(sentence))  # split the sentence into single characters

encoded_text = []
for letter in delimit:  # iterates through list uses dictionary to get value and append to encoded_text list
    letter_num = lower_letters.get(letter)
    encoded_text.append(letter_num)

print(encoded_text)

# created list for keys and values
key_list = list(lower_letters.keys())
val_list = list(lower_letters.values())

coded_msg = []
user_input = (input('Type in coded message (separate by space): '))
x = user_input.split(" ")  # takes user_input and separates string into items in list
for i in x:  # reiterates through items in list and coverts to integer. adds items to coded_msg list
    convert = int(i)
    coded_msg.append(convert)

decoded_text = []
for num in coded_msg:  # decodes the text
    decoded_text.append(list(lower_letters.keys())[list(lower_letters.values()).index(num)])

print(*decoded_text, sep='')  # prints decoded message and removes quotations

#todo create dictionary for upper case letters, numbers, symbols
#todo create try catch blocks to capture errors