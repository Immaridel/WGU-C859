def swap(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
