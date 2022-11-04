# Binary Search Algorithm

# Get player name
player = input('I will try to guess your number. Please enter your name: ')

def print_hi(name):
    # function to greet player
    print(f'Hi, {name}')

# Counter function
def searcher():
    # Get number guess
    number = int(input('Please enter a number between 1 and 100: '))
    if number < 50:
        print('Your number is less than 50')
    else:
        print('Greater than or equal to 50')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(player)
    searcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
