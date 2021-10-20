n,k = [int(i) for i in input().split()]
h = sorted([int(input()) for _ in range(n)])
m = 1000000000
for i in range(n-k+1):
  m = min((h[i+k-1]-h[i]),m)
print(m)