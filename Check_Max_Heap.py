import heapq
def checkMaxHeap(lst):
    orig = lst[:]
    heapq._heapify_max(lst)
    
    if lst == orig:
        return True
    return False

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
