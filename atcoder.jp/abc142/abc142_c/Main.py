n = int(input())
a = list(map(int,input().split()))
a_enu = [(i+1, s) for i, s in enumerate(a)]
a_enu_st = sorted(a_enu, key=lambda x: x[1])
for c in (a_enu_st):
  print(c[0], end=' ')