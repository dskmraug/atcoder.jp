a,b = [int(i) for i in input().split()]
ans = 1
for c in range(a-b):
  ans = ans * 32
print(ans)