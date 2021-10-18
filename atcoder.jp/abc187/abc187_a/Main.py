x = list(map(str,input().split()))

suma = int(x[0][0]) + int(x[0][1]) + int(x[0][2])
sumb = int(x[1][0]) + int(x[1][1]) + int(x[1][2])

print(max(suma,sumb))