n = int(input())
a = list(map(int, input().split()))
fst = (0,0)
sec = (0,0)
if (a[0] > a[1]):
  fst = (0,a[0])
  sec = (1,a[1])
else:
  sec = (0,a[0])
  fst = (1,a[1])
for i in range(2,n):
  if (a[i] < sec[1]):
    continue
  elif (a[i] > fst[1]):
    sec = fst
    fst =(i,a[i])
  else:
    sec =(i,a[i])
print(sec[0]+1)