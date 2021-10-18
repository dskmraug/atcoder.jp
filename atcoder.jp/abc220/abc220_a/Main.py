a,b,c = [int(i) for i in input().split()]
ans = -1
for i in range (1000):
  c = c*(i+1)
  if a <= c <= b:
    ans = c
    break
  if c > 1000:
    break
print(ans)