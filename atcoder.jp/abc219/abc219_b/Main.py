s = [str(input()) for _ in range(3)]
t = str(input())
ans = ""
for c in t:
  if (c == "1"):
    ans += s[0]
  elif(c == "2"):
    ans += s[1]
  else:
    ans += s[2]
print(ans)