from stackBasis.stack import Stack

def postfix_eval(expression):

    op_stack = Stack()

    token_list = expression.split()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            operand2 = op_stack.pop()
            operand1 = op_stack.pop()
            result = calc(token, operand1, operand2)
            op_stack.push(result)

    return op_stack.pop()


def calc(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval('7 8 + 3 2 + /'))