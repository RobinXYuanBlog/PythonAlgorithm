from time import time


def shell_sort(A):
    count = len(A)
    # Initial gap
    inc = round(count / 2)
    while inc > 0:
        for i in range(inc, count-1):
            # For every gap, do the insertion sort
            temp = A[i]
            j = i
            while (j >= inc) and (A[j - inc] > temp):
                A[j] = A[j - inc]
                j = j - inc
            A[j] = temp
        # Get new gap
        inc = round(inc / 2)

    return A


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    start = time()
    shell_sort(LIST)
    stop = time()
    print(LIST)
    print(str(stop - start) + " second")