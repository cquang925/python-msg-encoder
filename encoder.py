from randomizer import characters


# created definition that returns a list
def splitter(message):
    return list(message)


encoded_text = []


def encoder():
    sentence = input('Write a short sentence: ')
    delimit = (splitter(sentence))  # split the sentence into single characters

    for letter in delimit:  # iterates through list uses dictionary to get value and append to encoded_text list
        letter_num = characters.get(letter)
        encoded_text.append(letter_num)

    print(encoded_text)


#  saved encoded message to txt file
def save_encoded_msg():
    secret_msg = open('message.txt', 'w')
    for element in encoded_text:
        secret_msg.write(element + '\n')
    secret_msg.close()
