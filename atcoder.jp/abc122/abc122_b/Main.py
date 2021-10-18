s = input()
res = 0
m = 0
for c in s:
  if (c == "A" or c == "C" or c == "G" or c == "T"):
    res += 1
  else:
    res = 0
  m = max(res,m)
print(m)