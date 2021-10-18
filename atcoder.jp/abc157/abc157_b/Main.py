a = [list(map(int, input().split())) for _ in range(3)]
c = [[0,0,0],[0,0,0],[0,0,0]]
n = int(input())
ans = False
for _ in range(n):
  b = int(input())
  for i in range(3):
    for j in range(3):
      if (a[i][j] == b):
        c[i][j] = 1
ct = [list(x) for x in zip(*c)]
cx1 = [c[0][0],c[1][1],c[2][2]]
cx2 = [c[0][2],c[1][1],c[0][2]]
#print(c)
#print(ct)
chk = [1,1,1]
if(any([c[i] == chk for i in range(3)])):
  ans = True
elif(any([ct[i] == chk for i in range(3)])):
  ans = True
elif((cx1 == chk) or (cx2 == chk)):
  ans = True
else:
  ans = False
print("Yes") if(ans) else print("No")