def binarySearch(arr, x, left, right):
    '''
    Recursive binary search.

    arr (list or array) : array (or list) to be searched. Should be sorted in ascending
    x (object)          : object to be searched from the given array
    left (int)          : left most index value
    right (int)         : right most index value

    Returns (int)       : -1 if object x is not found in arr. Else index of the first occurence of object found is returned
    '''

    # check no result
    if left <= right:

        # find middle element
        mid = left + (right - left) // 2

        # compare with element to be searched
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binarySearch(arr, x, left, mid-1)
        else:
            return binarySearch(arr, x, mid+1, right)
    
    # element not found
    else:
        return -1

def main():

    arr = [1,2,3,4,5,6,7]
    x = 4

    result = binarySearch(arr, x, 0, len(arr)-1)
    if result == -1:
        print(f"Object {x} not found in the given array!")
    else:
        print(f"Object {x} found at index {result} of the given array!")

    x = 99
    result = binarySearch(arr, x, 0, len(arr)-1)
    if result == -1:
        print(f"Object {x} not found in the given array!")
    else:
        print(f"Object {x} found at index {result} of the given array!")

if __name__=='__main__':
    main()