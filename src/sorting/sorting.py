# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements #creates a list of 0's 
    #[0 for _ in range(elements)] is another way to do this

    # Your code here
    #start pointers at the start of both lists
    #compare value of pointers and smallest gets added to merge list
    #increment pointer to move onto next list
    
    #initialize each list for both pointers
    a = 0
    b = 0
    
    #loop through merged_arr
    for i in range(len(merged_arr)):
        #make sure pointer is in range of array
        #if it is out of range, copy other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]: #both indices are in range of their own array
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

            
    return merged_arr

#     while a < len(arrA) and b < len(arrB):
#         if arrA[a] < arrB[b]:
#             combined.append(arrA[a])
#             a += 1
#         else:
#             combined.append(arrB[b])
#             b +=1
            
#         #this will create the combined list
    
#         while a < len(arrA):
#              combined.append(arrA[a])
#              a += 1
#         while b < len(arrB):
#              combined.append(arrB[b])
#              b += 1
            
#         return combined


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass

# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass
