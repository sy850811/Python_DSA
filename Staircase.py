## Read input as specified in the question.
## Print output as specified in the question.
def staircase(current,target):
    if current == target:
        return 1
    elif current > target:
        return 0
    
    a = staircase(current + 1,target)
    b = staircase(current + 2,target)
    c = staircase(current + 3,target)
    
    return a + b + c

print(staircase(0,target = int(input())))
