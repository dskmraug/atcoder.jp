w=input()
bool=1
for i in range(len(w)):
  cnt = 0
  for j in range(len(w)):
    if (w[i]==w[j]):
      cnt += 1
  if (cnt%2==0):
    continue
  else:
    bool=0
    break
print("Yes") if bool else print("No")