a, b = [int(i) for i in input().split()]
if (a<=0 and 0<=b):
  ans = "Zero"
elif a>0:
  ans = "Positive"
else:
  if int(b-a+1)%2==0:
    ans = "Positive"
  else:
    ans = "Negative"
print(ans)