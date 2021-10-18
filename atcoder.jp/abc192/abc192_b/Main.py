s = input()
x = [0] * len(s)
for i,c in enumerate(s):
  if(i%2==0 and c.islower()):
    x[i]=1
  elif(i%2==1 and c.isupper()):
    x[i]=1
  else:
    continue
if(all(x)==1):
  print("Yes")
else:
  print("No")