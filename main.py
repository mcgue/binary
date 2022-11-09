# Binary Search Algorithm

# Get player name
player = input('I will try to guess your number. Please enter your name: ')


# Greeting function
def print_hi(name):
    # function to greet player
    print(f'Hi, {name}')

def get_response(num):
    confirm = input('Is your number less than {}? Y or N '.format(num))
    confirm = confirm[0].upper()
    return confirm

# Counter function
def searcher():
    # Get number guess
    response = get_response(50)
    while response != 'Y' and response != 'N':
        response = get_response()
    if response == 'Y':
        response = input('Is it less than 25? Y or N ')
    elif response == 'N':
        print('Greater than or equal to 50')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(player)
    searcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
