def towerofhanoi(n, source, aux, dest):
    if n == 0:
        return
    towerofhanoi(n-1,source,dest,aux)
    print(source,dest)
    towerofhanoi(n-1,aux,source,dest)

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
