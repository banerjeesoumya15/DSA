'''
Given a sorted array, find the greatest element,
less than or equal to the target element.

EXAMPLE:
arr = [1,4,6,8,9]
target = 7
Returns 6

arr = [12, 56, 78, 99]
target = 65
Returns 56
'''

def floor(arr, target):

    start = 0
    end = len(arr)-1
    mid = start + (end-start) // 2



    while(start<=end):
        
        if target==arr[mid]:
            return target
        
        elif target < arr[mid]:
            end = mid-1
        
        elif target > arr[mid]:
            start = mid + 1
        mid = start + (end-start) // 2
    
    return arr[end]

arr = [12, 56, 78, 99]
target = 65
print(floor(arr, target))

