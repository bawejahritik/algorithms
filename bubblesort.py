items = input("Enter array to be sorted : ").split()

for i in range(len(items)):
    items[i] = int(items[i])

for i in range(1, len(items)):
    for j in range(len(items)-1):
        if(items[j] > items[j+1]):
            items[j], items[j+1] = items[j+1], items[j]

print(items)