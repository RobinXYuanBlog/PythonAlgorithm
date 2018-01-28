from time import time


def insertion_sort(A):
    for j in range(2, len(A)):
        key = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    start = time()
    insertion_sort(LIST)
    stop = time()
    print(LIST)
    print(str(stop - start) + "second")