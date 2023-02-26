array = [1,5,8,11,18,23,30]

element = 23
low = 0
high = len(array) - 1
mid = (low + high) // 2


while low < high:
    if element == array[mid]:
        print(f"Element is present at index {mid}.")
        break

    elif element < array[mid]:
        high = mid - 1
        mid = (high + low) // 2

    else:
        low = mid + 1
        mid = (high + low) // 2