x = int(input())
ans = 0
if (x%100==0):
  ans = 100
else:
  ans = (100 - (x%100))
print(ans)