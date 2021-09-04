from sys import stdin
from sys import maxsize as MAX_VALUE
import sys
import math
sys.setrecursionlimit(200000)

#iterative
def minNoOfSquares(n) :
    mem = [1 if (math.sqrt(i) == int(math.sqrt(i))) else MAX_VALUE for i in range (n+1)]
    i = 1
    while i < n:
        j = 1
        while i + j*j <= n:
            if mem[i + j*j] > mem[i]+ 1:
                mem[i + j*j] = mem[i] + 1
            j+=1
        i+=1
    return mem[-1]

#recursive
# def minNoOfSquares(n):
#     if n == 0:
#         return 0
#     minStep = MAX_VALUE
#     for i in range(1,int(math.sqrt(n))+1):
#         temp = minNoOfSquares(n - i*i)
#         minStep = min(minStep, temp) + 1
#     return minStep

# recursive + memorization
# def minNoOfSquares(n,mem):
#     if n == 0:
#         return 0
#     if mem[n] != -1:
#             return mem[n]
#     minStep = MAX_VALUE
#     for i in range(1,int(math.sqrt(n))+1):
#         temp = minNoOfSquares(n - i*i,mem) + 1
#         minStep = min(minStep, temp)
#     mem[n] = minStep
        
#     return minStep


#main
n = int(stdin.readline().rstrip())
# mem = [-1 for i in range(n+1)]
# print(minNoOfSquares(n,mem))
print(minNoOfSquares(n))
