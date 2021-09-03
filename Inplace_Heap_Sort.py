def perculateDown(arr,i,n):
    pi =  i
    
    while 2*pi + 1 < n:
        cia = 2*pi + 1
        cib = 2*pi + 2
        ci = pi
        if arr[cia] < arr[pi]:
            ci = cia
        if cib < n and arr[cib] < arr[ci]:
            ci = cib
        if ci == pi:
            return
        arr[ci],arr[pi] = arr[pi],arr[ci]
        pi = ci

def createHeap(arr):
    for i in range(len(arr)//2 - 1,-1,-1):
        perculateDown(arr,i,len(arr))

def sort(arr):
    for i in range(len(arr) - 1 , -1, -1):
        # print(arr)
        arr[0],arr[i] = arr[i],arr[0]
        perculateDown(arr,0,i)
        
def heapSort(arr):
    createHeap(arr)
    sort(arr)

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')
