array = [8, 7, 9, 1, 2, 2]
smallestNum = 0

for i in range(len(array) - 1):
    smallestNum = i
    
    #swap with smallest number
    for j in range(i, len(array)):
        if array[j] < array[smallestNum]:
            smallestNum = j
        
    if array[i] != array[smallestNum]:
        #Swap
        array[smallestNum], array[i] = array[i], array[smallestNum]

    print(array)