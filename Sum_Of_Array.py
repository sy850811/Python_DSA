

def sum(li):
    if(len(li) == 0):
        return 0
    return int(li[0] + sum(li[1:]))
input()
print(sum([int(i) for i in input().split()]))
