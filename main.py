# Binary Search Algorithm
# import secrets for random number
import secrets

def rec_search(arr, low, high, x):
    # Calculate half point
    if high >= low:
        mid = (high + low) // 2

        # Check if already matches
        if arr[mid] == x:
            return mid
        # If middle larger, then do search on lower half
        elif arr[mid] > x:
            return rec_search(arr, low, mid-1, x)
        # If middle lower, then do search on upper half
        else:
            return rec_search(arr, mid+1, high, x)
    # X not present
    else:
        return -1

# Run if main
if __name__ == '__main__':
    print('What is the range to search? Please enter a number!')
    bot = int(input('Lowest number? '))
    top = int(input('Highest number? '))
    list_search = list(range(bot, top+1, 1))
    x = secrets.randbelow(top+1)
    print('Found at index ' + str(rec_search(list_search, bot, top, x)))