import sys
a,b,c = list(map(int,input().split()))
num = 0
if (a==b and b==c and a%2==0):
  print("-1")
  sys.exit()
while True:
  if(a%2==1 or b%2==1 or c%2==1):
    break
  else:
    num += 1
    a,b,c = ((b/2 + c/2),(a/2 + c/2),(a/2 + b/2))
print(num)