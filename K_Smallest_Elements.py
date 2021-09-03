import heapq
def kSmallest(lst, k):
    heapq.heapify(lst)
    abcd = []
    for i in range(k):
        abcd.append(heapq.heappop(lst))
    return abcd


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
