n = int(input())
x = [int(i) for i in input().split()]
su = int(sum(x) / n)
sum1 = 0
sum2 = 0
for j in range(n):
  sum1 += (x[j] - su) * (x[j] - su)
  sum2 += (x[j] - su-1) * (x[j] - su-1)
print(min(sum1,sum2))