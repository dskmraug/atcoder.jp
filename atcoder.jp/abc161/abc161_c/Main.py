n,k = list(map(int,input().split()))
ans = n
if (k==0):
  print("0")
else:
  ans = min(n%k,abs(n%k-k))
  print(ans)