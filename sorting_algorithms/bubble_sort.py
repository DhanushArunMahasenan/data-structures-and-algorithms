array = [8, 9, 7, 1, 2, 0]


for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            #swap(x, y = y, x)
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)