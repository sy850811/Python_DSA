## Read input as specified in the question.
## Print output as specified in the question.


def mul(add,count):
    if (count == 0):
        return 0
    return mul(add,count-1)+ add

from sys import setrecursionlimit
setrecursionlimit(110000)
add = int(input())
count = int(input())
print(mul(add,count))
