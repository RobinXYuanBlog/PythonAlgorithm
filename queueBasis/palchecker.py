from queueBasis.dequeue import Dequeue


def palchecker(text):
    deque = Dequeue()

    for char in text:
        deque.addRear(char)

    equal = True

    while deque.size() > 1 and equal:
        first = deque.removeFront()
        last = deque.removeRear()

        if first != last:
            equal = False

    return equal


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))