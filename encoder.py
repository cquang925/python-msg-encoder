from randomizer import characters


# created definition that returns a list
def splitter(message):
    return list(message)


encoded_text = []


def encoder():
    if len(encoded_text) != 0:
        encoded_text.clear()  # clears the list to ensure it is empty
    else:
        pass
    sentence = input('Write a short sentence: ')
    delimit = (splitter(sentence))  # splits the sentence into single characters and creates a list

    # iterates through delimit list and uses character dictionary to get values of characters.
    # appends encoded_text with values
    for letter in delimit:
        letter_num = characters.get(letter)
        encoded_text.append(letter_num)

    print(encoded_text, '\n')
    save_message = input('Would you like to save message? (y/n)')
    if save_message == 'y':
        save_encoded_msg()
        print('Message has been saved!\n')
    else:
        print('Message not saved. Returning to Main Menu.\n')


#  saved encoded message to txt file
def save_encoded_msg():
    secret_msg = open('message.txt', 'w')
    for element in encoded_text:
        secret_msg.write(element + '\n')
    secret_msg.close()
