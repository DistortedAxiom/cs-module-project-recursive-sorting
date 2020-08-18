# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    k = 0

    a = 0

    b = 0

    # Your code here
    while a < len(arrA) and b < len(arrB):

        if arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1

        else:
            merged_arr[k] = arrB[b]
            b += 1

        k += 1

    while a < len(arrA):
        merged_arr[k] = arrA[a]
        a += 1
        k += 1
    while b < len(arrB):
        merged_arr[k] = arrB[b]
        b += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) > 1:

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        arr = merge(merge_sort(left), merge_sort(right))

        return arr

    else:

        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
