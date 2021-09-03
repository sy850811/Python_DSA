# def index(li,x):
#     if len(li) == 0:
#         return -1
#     if li[0] == x:
#         return 0
#     else:
#         i = index(li[1:],x)
#         if i != -1:
#             return i+1
#         else:
#             return i

def index(li,s,x):
    if s == len(li):
        return -1
    if li[s] == x:
        return s
    else:
        return index(li,s+1,x)
int(input())
li = [ int(i) for i in input().split()]
x = int(input())
print(index(li,0,x))
