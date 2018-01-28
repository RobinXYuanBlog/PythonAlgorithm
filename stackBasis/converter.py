from stackBasis.stack import Stack


def convert_binary(dec_num):

    stack = Stack()

    while dec_num > 0:
        rem = dec_num % 2
        stack.push(rem)
        dec_num = dec_num // 2

        binary_string = ""

    while not stack.isEmpty():
        binary_string = binary_string + str(stack.pop())

    return binary_string


print(convert_binary(22))

