# Binary Search Algorithm
# User chooses a method

# Get player name
def get_method():
    def format_response():
        response = input('Recursive or Iterative? R or I ')[0].upper()
        return response

    # Choose recursive or iterative
    method_type = format_response()
    while method_type != 'R' and method_type != 'I':
        method_type = format_response()
    return method_type

# Function to guess number
def searcher():
    # Get number guess
    response = get_response(50)
    if response == 'Y':
        response = get_response(25)
        if response == 'Y':
            response = get_response(12)
            if response == 'Y':
                print('Number less than 12')
        else:
            print('between 25 and 49')
    elif response == 'N':
        print('Greater than or equal to 50')

def rec_search(arr):
    high = arr[-1]
    low = arr[0]
    return high, low

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('What is the range to search?')
    bot = int(input('Lowest number? '))
    top = int(input('Highest number? '))
    list_search = list(range(bot, top+1, 1))

    ans = get_method()
    if ans == 'R':
        print(rec_search(list_search))
    else:
        print('not R')

