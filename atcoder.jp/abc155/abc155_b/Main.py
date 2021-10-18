n = int(input())
a = list(map(int,input().split()))
even = [x for x in a if x%2 == 0]
if (len(even) == 0):
  print("APPROVED")
else:
  print("APPROVED") if (all((x%3==0) or (x%5==0)  for x in even)) else print("DENIED")
  