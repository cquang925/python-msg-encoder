from randomizer import characters


key_list = list(characters.keys())
val_list = list(characters.values())

coded_msg = []


# has user inputs coded message to decipher message
def decoder():
    user_input = (input('Type in coded message (separate by space): '))
    x = user_input.split(" ")  # takes user_input and separates string into items in list
    for i in x:  # reiterates through items in list and appends to coded_msg
        coded_msg.append(i)

    decoded_text = []
    for num in coded_msg:  # decodes the text
        decoded_text.append(list(characters.keys())[list(characters.values()).index(num)])

    print(*decoded_text, sep='')  # prints decoded message and removes quotations
