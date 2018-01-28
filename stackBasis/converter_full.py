from stackBasis.stack import Stack


def converter(dec_num, base):

    digits = "0123456789ABCDEF"

    stack = Stack()

    while dec_num > 0:
        rem = dec_num % base
        stack.push(rem)
        dec_num = dec_num // base

    result_string = ""

    while not stack.isEmpty():
        result_string = result_string + digits[stack.pop()]

    return result_string


print(converter(25, 2))
print(converter(334, 16))