n = int(input())
h = list(map(int,input().split()))
ans = 0
cnt = 0
for i in range(1,n):
  if (h[i]<=h[i-1]):
    cnt += 1
  else:
    cnt = 0
  ans = max(cnt,ans)
print(ans)