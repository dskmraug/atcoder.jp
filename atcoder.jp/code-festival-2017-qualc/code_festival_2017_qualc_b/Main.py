n=int(input())
a=list(map(int,input().split()))
even = [x for x in a if x%2 == 0]
ans = 3**n - 2**len(even)
print(ans)