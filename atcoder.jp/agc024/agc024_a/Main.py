import sys
a, b, c, k = [int(i) for i in input().split()]
print (a-b) if k%2==0 else print(b-a)