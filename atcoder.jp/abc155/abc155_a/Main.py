a, b, c = [int(i) for i in input().split()]
if (a==b and b!=c):
  bool = 1
elif (b==c and c!=a):
  bool = 1
elif (a==c and c!=b):
  bool = 1
else:
  bool = 0
print("Yes") if(bool) else print("No")