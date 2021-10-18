p = int(input())
src = [3628800,362880,40320,5040,720,120,24,6,2,1]
ans = 0
for i in range(10):
  for _ in range(10000000):
    if (p>=src[i]):
      p -= src[i]
      ans += 1
    else:
      break
print(ans)