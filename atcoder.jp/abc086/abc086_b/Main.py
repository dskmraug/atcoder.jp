a,b = list(map(str,input().split()))
m=int(a+b)
def is_square_num(n):
  i2 = 0
  for i in range(0, n + 1):
    if i2 == n:
      return True
    if i2 > n:
      return False
    i2 += i * 2 + 1

print("Yes") if is_square_num(m) else print("No")