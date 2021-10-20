txt = input()
if ((txt.count("N") >= 1) ^ (txt.count("S") >= 1)) != 0 or ((txt.count("E") >= 1) ^ (txt.count("W") >= 1)) != 0 :
  print("No")
else:
  print("Yes") 