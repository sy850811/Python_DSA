import heapq
def kthLargest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    heap=lst[:k]
    heapq.heapify(heap)
    n1=len(lst)
    for i in range(k,n1):
        if lst[i]>heap[0]:
           heapq.heappop(heap)        
           heapq.heappush(heap,lst[i])          
    return heap[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
