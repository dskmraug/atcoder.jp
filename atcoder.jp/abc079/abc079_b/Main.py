n = int(input())
li = [0] * 87
li[0] = 2
li[1] = 1
if n>=2:
  for i in range(2,n+1):
    li[i] = li[i-1] + li[i-2]
print(li[n])