
items = input("Enter array to be sorted : ").split()

for i in range(len(items)):
    items[i] = int(items[i])

#insertion sort

for i in range(1, len(items)):
    j = i
    while(j > 0 and items[j-1] > items[j]):
        items[j], items[j-1] = items[j-1], items[j]
        j -= 1

print(items)