x = int(input())
if x < 10:
  print("000" + str(x))
elif x < 100:
  print("00" + str(x))
elif x < 1000:
  print("0" + str(x))
else:
  print(x)