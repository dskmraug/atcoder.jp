n = int(input())
s = str(input())
cnt = 0
for c in range(n):
  cnt += 1
  if (s[c] == "1"):
    break
print("Takahashi") if cnt%2==1 else print("Aoki") 