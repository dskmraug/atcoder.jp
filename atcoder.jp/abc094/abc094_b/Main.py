n,m,x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
res = 0
for i in range(m):
  if (x<a[i]):
    res = i
    break  
print(min(res,m-res))