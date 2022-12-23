# Binary Search Algorithm
# import secrets for random number
import secrets

def rec_search(arr, low, high, x):
    # Check low < high and if already matches
    if high >= low:
        mid = (low + high)//2
        # Check if already matches
        if arr[mid] == x:
            return mid
        # If middle larger, then do search on lower half
        elif arr[mid] > x:
            return rec_search(arr, low, high-1, x)
        # If middle lower, then do search on upper half
        else:
            return rec_search(arr, low+1, high, x)
    else:
        return -1

# Run if main
if __name__ == '__main__':
    # Generate sorted list
    list_search = list(range(0, 11, 2))
    print(list_search)
    # Set low and high
    low = 0
    high = len(list_search)-1
    # Generate number to search
    x = int(secrets.randbelow(11))
    print(x)
    result = rec_search(list_search, low, high, x)
    if result == -1:
        print('Not found')
    else:
        print(str(x) + ' found at index ' + str(result))