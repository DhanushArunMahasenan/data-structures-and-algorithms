def LinearSearch(sortedNums, random_num):
    linear_counter = 0

    for j in range(len(sortedNums)):
        if sortedNums[j] == random_num:
            #print(f"Number found at index: {j}.")
            break
        
        linear_counter += 1

    return linear_counter



