import encoder
import decoder
import randomizer

print("**********Main Menu**********")
print("""    1.Encode a message
    2.Decode a message
    3.Create key
    4.View//Print key
    5.Quit""")
choice = input("What would you like to do: ")

if choice == '1':
    print()
    randomizer.import_key()
    encoder.encoder()

elif choice == '2':
    print()
    randomizer.import_key()
    decoder.decoder()

elif choice == '3':
    randomizer.randomize()
    randomizer.save_key()
    print('Key has been created successfully')
    view_key = input('Would you like to view the key?(y/n) ')
    if view_key == 'y':
        print(randomizer.characters)
    elif view_key == 'n':
        print('Okie dokie')

elif choice == '4':
    randomizer.import_key()
    randomizer.view_key()

elif choice == '5':
    print('Good-bye. Have a good day!')

else:
    print('Invalid selection. Please select a valid option')

# todo create try catch blocks to capture errors
# todo create loop to return to main menu