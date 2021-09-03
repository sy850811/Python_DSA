def convertArrayToDict(l):
    d = {}
    for i in l:
        if d.get(i,False):
            d[i] += 1
        else:
            d[i] = 1
    return d

def printPairDiffK(l, k):
    d = convertArrayToDict(l)
    count = 0
    for i in d.keys():
        if d.get(i+k,False):
            if k ==0:
                count += (d[i]*(d[i] - 1)// 2)
            else:
                count += d[i] * d[i+k]
    return count
    
    
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
