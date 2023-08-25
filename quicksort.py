import random

def part(arr,start,stop):
	pivot = start # pivot
	
	i = start + 1

	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =\
			arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

def partition(arr, lo, hi):
    idx = random.randrange(lo, hi)
    arr[lo], arr[idx] = arr[idx], arr[lo]
    return part(arr, lo, hi)
    

def quickSort(arr, lo, hi):
    if lo<hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)
    



items = [5, 4, 3, 2 ,1]

for i in range(len(items)):
    items[i] = int(items[i])

quickSort(items, 0, len(items)-1)
print(items)

# Python implementation QuickSort using
# Lomuto's partition Scheme.
