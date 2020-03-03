from randomizer import characters


key_list = list(characters.keys())
val_list = list(characters.values())

coded_msg = []


# has user input a coded message to decode
def user_msg():
    coded_msg.clear()
    user_input = (input('Type in coded message (separate by space): '))
    x = user_input.split(" ")  # takes user_input and separates string into items in list
    for i in x:  # reiterates through items in list and appends to coded_msg
        coded_msg.append(i)
    decoder()


# imports message from 'coded message.txt' and runs through decoder
def upload_msg():
    coded_msg.clear()
    with open("coded message.txt", 'r') as file:  # opens file
        for num in file:  # iterates through file
            num = num.strip()  # removes '\n' from each line
            coded_msg.append(num)  # adds to coded_msg
    file.close()  # closes file
    decoder()


# takes coded_msg and decodes message
def decoder():
    decoded_text = []
    for num in coded_msg:  # decodes the text
        decoded_text.append(list(characters.keys())[list(characters.values()).index(num)])

    print(*decoded_text, sep='',)  # prints decoded message and removes quotations
    print()


# todo make upload_msg more dynamic and able to import through long line
# todo create try/catch for user input errors and key not found errors
