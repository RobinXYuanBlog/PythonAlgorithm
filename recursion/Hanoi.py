# def hanoi(steps, left='left', right='right', middle='middle'):
#     if steps:
#         hanoi(steps - 1, left, middle, right)
#         print(left, '=>', right)
#         hanoi(steps - 1, middle, right, left)
#


# 3 0 0
# 2 0 1
# 1 1 1
# 1 2 0
# 0 2 1
# 1 1 1
# 1 0 2
# 0 0 3

def hanoi(steps, left='left', middle='middle', right='right'):
    if steps:
        hanoi(steps - 1, left, right, middle)
        print(left, '=>', right)
        hanoi(steps - 1, middle, left, right)


hanoi(3)