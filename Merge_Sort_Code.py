# def merge(a,b,l,k):
#     i,j = 0,0
#     # print("a,b=",a,b)
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             l[k] = a[i]
#             i+=1
#         else:
#             l[k] = b[j]
#             j+=1
#         k+=1
#     while i < len(a):
#         l[k] = a[i]
#         k+=1
#         i += 1
#     while j<len(b):
#         l[k] = b[j]
#         k+=1
#         j+=1

# def mergeSort(arr, start, end):
#     if end - start + 1 <= 1:
#         return
#     mid = (start+end)//2
#     mergeSort(arr,start,mid)
#     mergeSort(arr,mid+1,end)
#     merge(arr[start:mid+1],arr[mid+1:end+1],arr,start)

def merge(a,b,l):
    i,j,k = 0,0,0
    # print("a,b=",a,b)
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            l[k] = a[i]
            i+=1
        else:
            l[k] = b[j]
            j+=1
        k+=1
    while i < len(a):
        l[k] = a[i]
        k+=1
        i += 1
    while j<len(b):
        l[k] = b[j]
        k+=1
        j+=1
    return l
def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    mid = (len(arr)//2)
    a = mergeSort(arr[:mid])
    b = mergeSort(arr[mid:])
    return merge(a,b,arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
# mergeSort(arr, 0, n-1)
mergeSort(arr)
print(*arr)
