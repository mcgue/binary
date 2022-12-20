# Binary Search Algorithm
# import secrets for random number
import secrets

def rec_search(arr, low, high, x):
    # Calculate half point
    print(str(low) + ' ' + str(high))
    if high >= low:
        mid = low + (high - low) // 2

        # Check if already matches
        if arr[mid] == x:
            return mid
        # If middle larger, then do search on lower half
        elif arr[mid] > x:
            return rec_search(arr, low, mid, x)
        # If middle lower, then do search on upper half
        else:
            return rec_search(arr, mid+1, high, x)
    # X not present
    else:
        return -1

# Run if main
if __name__ == '__main__':
    # Get range to search
    print('What is the range to search? Please enter an integer.')
    while True:
        try:
            bot = int(input('Lowest number? '))
        except ValueError:
            print("Please enter a valid integer")
            continue
        else:
            print(f'You entered the low for the range: {bot}')
            break
    top = int(input('Highest number? '))
    list_search = list(range(bot, top+1, 1))
    print(list_search)
    # Generate number to search
    x = int(secrets.choice(list_search))
    print(x)
    print(str(x) + ' found at index ' + str(rec_search(list_search, bot, top, x)))