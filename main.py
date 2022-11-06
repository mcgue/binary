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
    response = response[0].upper()
    while response != 'Y' and response != 'N':
        response = input('Is your number less than 50? Y or N ')
        response = response[0].upper()
    if response == 'Y':
        response = input('Is it less than 25? Y or N ')
    elif response == 'N':
        print('Greater than or equal to 50')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(player)
    searcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
