n = int(input())
a = list(map(int,input().split()))
ans = 0

for c in a:
  if c>10 : ans += c-10 

print(ans)