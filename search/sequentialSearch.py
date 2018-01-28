

def squential_search(list, item):

    pos = 0
    found = False

    length = len(list)

    while pos < length and not found:
        if list[pos] == item:
            found = True
        else:
            pos += 1

    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(squential_search(testlist, 3))
print(squential_search(testlist, 13))