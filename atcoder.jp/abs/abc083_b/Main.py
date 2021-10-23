n, a, b = [int(i) for i in input().split()]
tot = 0
for i in range (1,n+1):
  tmp = i
  sum = 0
  while tmp > 0:
    sum += int(tmp%10)
    tmp = int(tmp/10)
  if (a<= sum and sum <= b) : tot += i
print(tot)