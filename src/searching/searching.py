# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end: #check base:target is midpoint
                    #or range of search space
    
        mid = (start + end) // 2
    
    #check if target is the actual mid
        if arr[mid] == target:
            return mid
    
    #check if target is smaller than mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid -1)
    
    #check if target is larger than mid
        else:
            return binary_search(arr, target, end, mid + 1)
    
    #target is not in array return down to end
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    
    #base will be random
    if arr[0]
    # Your code here

