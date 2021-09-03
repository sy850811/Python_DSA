from sys import stdin
from sys import maxsize as MAX_VALUE
import sys
sys.setrecursionlimit(200000)


# def countMinStepsToOne(n,mem) :
#     if n <=0:
#         return 0
#     if mem[n] != -1:
#         return mem[n]
    
#     divByThree,divByTwo = MAX_VALUE,MAX_VALUE
    
#     if n%3 == 0:
#         divByThree = countMinStepsToOne(n//3,mem)
    
#     if n%2 == 0:
#         divByTwo = countMinStepsToOne(n//2,mem)
    
#     subByOne = countMinStepsToOne(n-1,mem)
#     mem[n] = 1 + min(divByThree,divByTwo,subByOne)
    -
#     return mem[n]
    
def countMinStepsToOne(n) :
    mem = [MAX_VALUE for i in range (n+1)]
    mem[1] = 0
    i = 1
    while i < n:
        
        if i + 1 <= n:
            mem[i+1] = min(mem[i+1],mem[i]+1)
        
        if 2*i <= n:
            mem[2*i] = min(mem[2*i],mem[i]+1)
        
        if 3*i <= n:
            mem[3*i] = min(mem[3*i],mem[i]+1)
        
        i += 1
    return mem[-1]
    



#main
n = int(stdin.readline().rstrip())
# mem = [-1 for i in range (n+1)]
# mem[1] = 0
# print(countMinStepsToOne(n,mem))
print(countMinStepsToOne(n))
