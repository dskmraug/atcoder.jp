s=input()
[a,b,c,d] = [int(s[0]),int(s[1]),int(s[2]),int(s[3])]
for i in range (8):
  [b1,b2,b3] = [int(i/4),int((i%4)/2),int((i%4)%2)]
  op1 = "+" if b1 == 0 else "-"
  op2 = "+" if b2 == 0 else "-"
  op3 = "+" if b3 == 0 else "-"
  if (a + b*(-1)**b1 + c*(-1)**b2 + d*(-1)**b3 == 7):
    print(s[0]+op1+s[1]+op2+s[2]+op3+s[3]+"=7")
    break