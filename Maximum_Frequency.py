from sys import stdin
def maxfreq(arr):
    d = {}
    for i in arr:
        if i in d:
          d[i]+=1
        else:
          d[i] = 1
    mfNum = -1
    mf = 0
    for num in arr:
      if d[num] > mf:
        mfNum = num
        mf = d[num]
    return mfNum
    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))

