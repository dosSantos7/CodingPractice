ll = [1,2,3,6,8,9,12,15,18]

def binary_search(arr, l, r, target):
    if l <= r:  # this is important
        m = l + (r-l) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            return binary_search(arr, m+1, r, target)
        else:
            return binary_search(arr, l, m-1, target)
    else: 
        return -1

print(binary_search(ll, 0, len(ll)-1, 18)) 