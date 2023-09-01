arr = input("Enter sorted array: ").split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

target = int(input("Enter target element: "))

left = 0
right = len(arr)-1

ans = -1

while left<=right:
    mid = (left+right)//2

    if arr[mid] == target:
        ans = mid
        break
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid-1

print(ans)