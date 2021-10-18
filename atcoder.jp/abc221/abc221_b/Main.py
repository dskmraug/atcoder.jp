s = list(input())
t = list(input())
n = int(len(s))
bool = 0
if s == t:
  bool = 1
else:
  for c in range (0,n-1):
    s[c], s[c+1] = s[c+1], s[c]
    if s == t:
      bool = 1
      break
    else:
      s[c], s[c+1] = s[c+1], s[c]
if (bool):
  print("Yes")
else:
  print("No")