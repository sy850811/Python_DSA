## Read input as specified in the question.
## Print output as specified in the question.

def countZero(n):
    if n == 0:
        return 0
    if (n%10 == 0):
        return 1 + countZero(n//10)
    else:
        return countZero(n//10)

n = int(input())
if n == 0:
        print("1")
else:
        print(countZero(n))
