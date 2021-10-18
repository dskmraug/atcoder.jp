n, x = [int(i) for i in input().split()]
a=list(map(int,input().split()))
for o in a:
  if (o == x):
    continue
  else:
    print(o, end=' ')