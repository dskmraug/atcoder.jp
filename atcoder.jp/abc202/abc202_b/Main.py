s=str(input())
st=s[::-1]
ans = ""
for c in st:
  if (c == "6") :
    ans +="9"
  elif (c == "9") :
    ans +="6"
  else:
    ans +=c
print(ans)