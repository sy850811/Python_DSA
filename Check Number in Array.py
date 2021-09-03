def find(li,x):
    if(len(li) == 0):
        return False
    if(li[0] == x):
        return True
    else:
        return find(li[1:],x)
input()

li = [int(i) for i in input().split()]
x = int(input())
if find(li,x):
    print("true")
