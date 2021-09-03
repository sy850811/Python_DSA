from sys import stdin

def pairSum0(l,n):
    # making dict
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
    # count begins
    count = 0
    if d.get(0,False):
        count = d[0]*(d[0]-1)//2
        d[0] = 0
    for i in d.keys():
        if d.get(-1 * i,False):
            count += d[i] * d[-1*i]
            d[i] = 0
            d[-1*i] = 0
    return count
                
    










    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
