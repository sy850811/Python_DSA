## Read input as specified in the question.
## Print output as specified in the question.

def digisum(n):
    if n == 0:
        return 0
    return n%10 + digisum(n//10)
print(digisum(int(input())))
