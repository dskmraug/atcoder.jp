a,b = [int(i) for i in input().split()]
ans = 0
if (b == 1):
  ans=0
else:
  for i in range(1,20):
    if ((a-1) * (i-1) + a >= b):
      ans = i
      break
    else:
      continue
print(ans)