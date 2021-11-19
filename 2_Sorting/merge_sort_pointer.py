ll = [4,5,2,1,3,6,9,8,7]

def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    left = []
    right = []

    for i in range(0, n1):
        left.append(arr[l + i])
    
    for i in range(0, n2):
        right.append(arr[m+1+i])
    
    i = j = 0
    k = l

    while i< n1 and j<n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    
    while i< n1:
        arr[k] = left[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k] = right[j]
        j+=1
        k+=1
    
    return arr

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        return merge(arr, l, m, r)

print(merge_sort(ll, 0, len(ll)-1))