p = [int(i) for i in input().split()]
q = ""
num2alpha = lambda c: chr(c+96)
for i in range (len(p)):
  q += num2alpha(p[i])
print(q)