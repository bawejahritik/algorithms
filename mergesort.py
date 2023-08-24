def merge(arr1, arr2):
    i, j = 0, 0
    res = []
    print(arr1)
    print(arr2) 
    while i<len(arr1) and j<len(arr2):
        if(arr1[i] < arr2[j]):
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j+=1

    if(i < len(arr1)):
        while(i < len(arr1)):
            res.append(arr1[i])
            i += 1
    
    if(j < len(arr2)):
        while(j < len(arr2)):
            res.append(arr2[j])
            j += 1
    
    return res


def mergeSort(arr):
    if(len(arr) < 2):
        return arr
    mid = len(arr)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


# items = input("Enter array to be sorted : ").split()

items = [5, 4, 3, 2 ,1]

for i in range(len(items)):
    items[i] = int(items[i])


print(mergeSort(items))