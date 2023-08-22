def getSmallest(arr, si):
    minYet = float('inf')
    minIdx = -1
    for i in range(si, len(arr)):
        if(minYet > arr[i]):
            minYet = arr[i]
            minIdx = i
    
    return minYet, minIdx


items = input("Enter array to be sorted : ").split()

for i in range(len(items)):
    items[i] = int(items[i])

sort_idx = 0

while(sort_idx < len(items)):
    small, smallIdx = getSmallest(items, sort_idx)
    items[sort_idx], items[smallIdx] = items[smallIdx], items[sort_idx]
    sort_idx += 1 

print(items)


