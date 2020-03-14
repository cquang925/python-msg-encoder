#!/usr/bin/env python3
# Encoder encodes and decodes messages

from encoder import encoder
from decoder import user_msg, upload_msg
import randomizer
import pyinputplus as pyip

    if choice == 'Encode Message':
        print()
        try:
            randomizer.import_key()
        except FileNotFoundError:
            print("Please create key.")
        encoder()

    elif choice == 'Decode Message':
        print()
        try:
            randomizer.import_key()
        except FileNotFoundError:
            print("Please create key.")
        else:
            reply = pyip.inputChoice(['Key Message', 'Import Message'])
            if reply == 'Key Message':
                user_msg()
            elif reply == 'Import Message':
                upload_msg()

    elif choice == 'Create Key':
        randomizer.randomize()
        randomizer.save_key()
        print('\n Key has been created successfully')
        view_key = pyip.inputYesNo('Would you like to view the key?(y/n)\n')
        if view_key == 'yes':
            print(randomizer.characters + '\n')
        elif view_key == 'no':
            print('Returning to Main Menu \n')

    elif choice == 'View/Print Key':
        try:
            randomizer.import_key()
        except FileNotFoundError:
            print("Unable to find key file. \n")
        else:
            randomizer.view_key()

    elif choice == 'Quit':
        print('Have a good day! Good-bye.')
        break

# todo check to see if character dictionary is empty
