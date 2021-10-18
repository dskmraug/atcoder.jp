n, a, x, y = [int(i) for i in input().split()]
if (n > a):
  res = x * a + y * (n-a)
else :
  res = x * n
print(res)