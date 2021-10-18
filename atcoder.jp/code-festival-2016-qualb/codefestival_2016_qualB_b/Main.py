n,a,b = [int(i) for i in input().split()]
c = a + b
f = b
s = str(input())
for i in range(n):
  if (s[i]=="c"):
    print("No")
  elif (s[i]=="a"):
    if (c > 0):
      print("Yes")
      c -= 1
    else:
      print("No")
  else:
    if (c>0 and b > 0):
      print("Yes")
      c -= 1
      b -= 1
    else:
      print("No")
    