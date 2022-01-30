'''
Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.
USING GCD
'''

def rotate_gcd(arr, d, n):
    '''
    rotate 1-D array by d elements using GCD method
    '''
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
         
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

    return arr

def gcd(n,d):

    if d==0:
        return n
    else:
        return gcd(d, n%d)

def input_data():
    n = int(input("Enter total no. of elements in array: "))
    arr = input(f"Enter {n} elements separated by space: ")
    d = int(input("Enter number by which array is to be rotated: "))

    arr = arr.split(' ')
    return (arr, d, n)

def print_data(arr):

    for ele in arr:
        print(ele, end=' ')

def main():
    (arr, d, n) = input_data()
    rotate_gcd(arr, d, n)
    print_data(arr)

if __name__=='__main__':
    main()
