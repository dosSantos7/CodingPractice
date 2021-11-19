"""
Given a list, use merge sort to sort the list
"""

ll = [4,1,2,5,8,9,7,6,3]

def merge(left, right):
    output = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    output.extend(left[i:])
    output.extend(right[j:])
    return output

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left_sub = merge_sort(arr[:m])
    right_sub = merge_sort(arr[m:])
    return merge(left_sub, right_sub)

print(merge_sort(ll))