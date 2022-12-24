# Recursive Binary Search Algorithm

# import secrets module for random number
import secrets

def rec_search(arr, low, high, x):
    # Check low < high
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
    # return -1 if not found
    else:
        return -1

# Run if main
if __name__ == '__main__':
    # Set top of range
    top = 1000
    # Generate sorted list
    list_search = list(range(0, top, 3))
    print(list_search)
    # Set low and high for indices
    low = 0
    high = len(list_search)-1
    # Generate number to search
    x = int(secrets.randbelow(top))
    # Run function to search list
    result = rec_search(list_search, low, high, x)
    # print results of running search
    if result == -1:
        print(str(x) + ' not found in list.')
    else:
        print(str(x) + ' found at index ' + str(result))