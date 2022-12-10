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

def rec_search():
    statement = ('You selected recursive')
    return statement

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ans = get_method()
    if ans == 'R':
        print(rec_search())
    else:
        print('not R')

    #print(get_list())

    print('What is the range to search')
    bot = int(input('Bottom of the range? '))
    top = int(input('Top of the range? '))
    list_search = list(range(bot, top, 1))

    print(list_search)
