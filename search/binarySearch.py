

def binary_search(list, item):

    first_item = 0
    last_item = len(list) - 1

    found = False

    while first_item <= last_item and not found:
        mid_item = (first_item + last_item) // 2

        if list[mid_item] == item:
            found = True
        else:
            if item < list[mid_item]:
                last_item = mid_item - 1
            else:
                first_item = mid_item + 1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))