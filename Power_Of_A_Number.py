def pow_rec(x,n):
    if n == 0:
        return 1
    return x * pow_rec(x,n-1)

x,n = [int(i) for i in input().split()]

print(pow_rec(x,n))
