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
            response = get_response(12)
            if response == 'Y':
                print('Number less than 12')
        else:
            print('between 25 and 49')
    elif response == 'N':
        print('Greater than or equal to 50')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print (get_method())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
