import sys
h,w = [int(i) for i in input().split()]
a = [[int(a) for a in input().split()] for _ in range(h)]
bool=1
for i1 in range(h-1):
  for i2 in range(i1+1, h):
    for j1 in range(w-1):
      for j2 in range(j1+1, w):
        if a[i1][j1] + a[i2][j2] > a[i2][j1] +a[i1][j2]:
          print("No")
          bool=0
          sys.exit()
if (bool): print("Yes")