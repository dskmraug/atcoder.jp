m = int(input())
 
if m < 100:
    ans = '00'
elif 100 <= m <= 5000:
    a = int(m / 1000 * 10)
    if a < 10:
        ans = '0' + str(int(a))
    else:
        ans = str(int(a))
elif 6000 <= m <= 30000:
    a = int(m / 1000 + 50)
    ans = str(a)
elif 35000 <= m <= 70000:
    a = int((m / 1000 - 30) / 5 + 80)
    ans = str(a)
else:
    ans = '89'
 
print(ans)