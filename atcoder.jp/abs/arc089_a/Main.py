n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())
can = True
if t[0]-(x[0]+y[0]) < 0 or (t[0]-x[0]-y[0])%2 !=0:
  can = False
else:
  if n > 1:
    for i in range(1,n):
      chk = (t[i]-t[i-1]) - abs(x[i]-x[i-1]) - abs(y[i]-y[i-1])
      if chk < 0 or chk %2 !=0:
        can = False
        break
print("Yes") if can else print("No")