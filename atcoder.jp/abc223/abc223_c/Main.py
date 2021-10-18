n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
t_s = [0.0] * (n+1)
a_s = [0] * (n+1)
for i in range(0,n):
  t_s[i+1] = t_s[i] + a[i] / b[i]
  a_s[i+1] = a_s[i] + a[i]
te = t_s[n] / 2
for j in range(0,n):
  if (t_s[j] <= te < t_s[j+1]):
    print(a_s[j] + b[j] * (te - t_s[j]))
    break