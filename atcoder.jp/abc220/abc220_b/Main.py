k = int(input())
a, b = input().split()

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,(len(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out
a10 = Base_n_to_10(a,k)
b10 = Base_n_to_10(b,k)
ans = a10 * b10
print(ans)
