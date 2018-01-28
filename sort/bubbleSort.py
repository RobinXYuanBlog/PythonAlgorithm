from time import time


def bubble_sort(A):
    n = len(A)
    for i in range(0, n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    start = time()
    bubble_sort(LIST)
    stop = time()
    print(LIST)
    print(str(stop - start) + "second")

