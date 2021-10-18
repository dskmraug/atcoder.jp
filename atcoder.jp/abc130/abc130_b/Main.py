n, x = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
d = [0] * (n+1)
cnt = 1
for c in range (1,n+1):
  d[c] = d[c-1] + l[c-1]
  if d[c] <= x:
    cnt=cnt+1
print(cnt)