import itertools
n = int(input())
a = []
for i in range(n):
  a.append(list(map(int,input().split())))
ans = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if (((a[i][0] - a[k][0]) * (a[j][1] - a[k][1])) - ((a[j][0] - a[k][0]) * (a[i][1] - a[k][1]))) != 0:
        ans += 1
print(ans)