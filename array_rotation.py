'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 
'''

def rotate(ar, d, n):
    # store first d elements in temporary
    temp = ar[:d]
    
    # modify the given array
    ar = ar[d:]
    
    # append the temporary array to the end
    ar.extend(temp)
    return ar

def main():
    n = int(input("Enter number of elements: "))
    ar = input("Enter {} elements separated by space: ".format(n))
    d = int(input("Enter number of elements by which to rotate: "))
    
    ar = ar.split(' ')
    ar = rotate(ar, d, n)
    
    for ele in ar:
        print(ele, end=" ")

if __name__=='__main__':
    main()
