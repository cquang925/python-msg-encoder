#!/usr/bin/env python3
# Encoder encodes and decodes messages

from encoder import encoder
from decoder import user_msg, upload_msg
import randomizer
import pyinputplus as pyip

while True:
    print('~~~~~~~~~~ Main Menu ~~~~~~~~~~')
    choice = pyip.inputMenu(['Encode Message', 'Decode Message', 'Create Key', 'View/Print Key', 'Quit'], numbered=True)

    if choice == 'Encode Message':
        print()
        randomizer.import_key()
        encoder()

    elif choice == 'Decode Message':
        print()
        randomizer.import_key()
        reply = pyip.inputChoice(['Key Message', 'Import Message'])
        if reply == 'Key Message':
            user_msg()
        elif reply == 'Import Message':
            upload_msg()

    elif choice == 'Create Key':
        randomizer.randomize()
        randomizer.save_key()
        print('Key has been created successfully')
        view_key = input('Would you like to view the key?(y/n)\n')
        if view_key == 'y':
            print(randomizer.characters, '\n')
        elif view_key == 'n':
            print('Returning to Main Menu \n')

    elif choice == 'View/Print Key':
        randomizer.import_key()
        randomizer.view_key()

    elif choice == 'Quit':
        print('Have a good day! Good-bye.')
        break

# todo create try catch blocks to capture errors
# todo check to see if character dictionary is empty
