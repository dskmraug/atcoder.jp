n = int(input())
l = []
for i in range(n):
    s,t=input().split()
    l.append([s, int(t) , i+1])
ls= sorted(l, key=lambda x:(x[0], -x[1]),)
for i in range(n):
  print(ls[i][2])