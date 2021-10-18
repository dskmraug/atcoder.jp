n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
ans = 0
for i in range(n):
  for j in range(n):
    if (i<j):
      if (abs((y[j]-y[i]) / (x[j]-x[i])) <=1) :ans +=1
    else: continue
print(ans)