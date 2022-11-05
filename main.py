# Binary Search Algorithm

# Get player name
player = input('I will try to guess your number. Please enter your name: ')

def print_hi(name):
    # function to greet player
    print(f'Hi, {name}')

# Counter function
def searcher():
    # Get number guess
    response = input('Is your number less than 50? Y or N ')
    if response[0].upper() == 'Y':
        print('Your number is less than 50')
    elif response[0].upper() == 'N':
        print('Greater than or equal to 50')
    else:
        print('Please enter Y or N')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(player)
    searcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
