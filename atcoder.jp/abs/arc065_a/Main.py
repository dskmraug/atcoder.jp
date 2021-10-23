s = input()
div = ["dream", "dreamer", "erase", "eraser"]
sr = s[::-1]
divr = [""] *4
for c in range(4):
  divr[c] = div[c][::-1]
can = True
n=len(s)
while n>0:
  can2 = False
  for j in range(4):
    d = divr[j]
#    print(sr[(len(s)-n):])
    if sr[(len(s)-n):].startswith(d):
      can2 = True
      n -= len(d)
  if not can2:
    can = False
    break
print ("YES") if can else print("NO")