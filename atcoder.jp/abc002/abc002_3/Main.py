xa, ya, xb, yb, xc, yc = map(int, input().split())
ans = float((((xa-xc) * (yb-yc)) - ((xb-xc) * (ya-yc))) / 2.0)
if ans < 0: 
  ans = ans *(-1.0)
print(ans)