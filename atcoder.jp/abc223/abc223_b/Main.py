s = input()
n = len(s)
smax = s
smin = s
for i in range(0,len(s)):
  if ((s[i:]+s[:i]) < smin) : smin = (s[i:]+s[:i])
  if ((s[i:]+s[:i]) > smax) : smax = (s[i:]+s[:i])
print(smin)
print(smax)