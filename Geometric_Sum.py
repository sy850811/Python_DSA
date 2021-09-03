## Read input as specified in the question.
## Print output as specified in the question.

def gm(n):
    if n == 0:
        return 1
    return (1/2**n) + gm(n-1)

print("%.5f" % gm(int(input())))
    
