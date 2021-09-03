def partitioning(l,s,e):
    p = 0
    pe = l[s]
    #count
    for i in l[s+1:e+1]:
        if i <= pe:
            p += 1
    #swap
    l[s],l[s+p] = l[s+p],l[s]
    
    #partitioning
    i = s
    j = e
    
    for k in range(p):
        while l[i] <= pe and i < e:
            i += 1
        while l[j] > pe:
            j -= 1
        if i >= p+s:
            break
        l[i],l[j] = l[j],l[i]
    return s+p

def quickSort(arr, s, e):
    if(s >= e):
        return
    i = partitioning(arr,s,e)
    # print(arr,i+1,e)
    # return
    quickSort(arr,s,i-1)
    quickSort(arr,i+1,e)
    


        
        
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, len(arr) - 1)
print(*arr)


