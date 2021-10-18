n = int(input())
w = [int(i) for i in input().split()]
s = [0] * n
s[0] = w[0]
for c in range(1,n):
  s[c] = s[c-1] + w[c]
ans = s[n-1]
for d in range(1,n):
  ans = min(abs(s[n-1] - 2 * s[d]), ans)
  if ans == 0:
    break
print(ans)