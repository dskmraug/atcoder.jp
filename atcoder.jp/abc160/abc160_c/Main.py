k,n = list(map(int,input().split()))
a = list(map(int,input().split()))
b = [0] * n
for i in range(0,n-1):
  b[i] = a[i+1]-a[i]
b[n-1] = (k - a[n-1]) + a[0]
print(k-max(b))