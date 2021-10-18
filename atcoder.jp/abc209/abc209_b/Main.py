n, x =  [int(i) for i in input().split()]
a = list(map(int,input().split()))
for i in range(n):
  if i%2 == 1:
    a[i] -= 1
print("Yes") if x >= sum(a) else print("No")