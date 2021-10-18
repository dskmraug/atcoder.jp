w, h, x, y = [int(i) for i in input().split()]
ans1 = float(w*h/2)
ans2 = 0
if (x *2 == w) and (y *2 == h):
  ans2 = 1
print(ans1, ans2)