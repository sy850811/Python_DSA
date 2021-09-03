from sys import stdin
def findMin(i,dict):
    while True:
        i -= 1
        if not dict.get(i,False):
            return i+1

def findMax(i,dict):
    while True:
        i += 1
        if not dict.get(i,False):
            return i-1
def longestConsecutiveSubsequence(arr,n): 
    d = {}
    count = 0
    for i in arr:
        d[i] = [True,count]
        count +=1
    uMin,uMax = None,None
    sI = None
    diff = -1
    for i in arr:
        min = findMin(i,d)
        max = findMax(i,d)
        if max - min > diff or (max - min == diff and d[min][1] < d[uMin][1]):
            diff = max - min
            uMin,uMax = min,max              
    return [uMin,uMax]









def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
