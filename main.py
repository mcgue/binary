# Binary Search Algorithm

# Get player name
player = input('Choose a number between 0 and 100. I will try to guess your number. '
               'First, please enter your name: ')

# Get player name
def print_hi(name):
    # function to greet player
    print(f'Hi, {name}')

# Get valid response
def get_response(num):
    ans = input('Is your number less than {}? Y or N '.format(num))
    ans = ans[0].upper()
    while ans != 'Y' and ans != 'N':
        ans = get_response(num)
    return ans

# Function to guess number
def searcher():
    # Get number guess
    response = get_response(50)
    if response == 'Y':
        response = get_response(25)
        if response == 'Y':
            print('Number less than 25')
        else:
            print('between 25 and 49')
    elif response == 'N':
        print('Greater than or equal to 50')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(player)
    searcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
