a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
[na, da] = [10, a] if a%10 == 0 else [a%10, int(a/10+1)*10]
[nb, db] = [10, b] if b%10 == 0 else [b%10, int(b/10+1)*10]
[nc, dc] = [10, c] if c%10 == 0 else [c%10, int(c/10+1)*10]
[nd, dd] = [10, d] if d%10 == 0 else [d%10, int(d/10+1)*10]
[ne, de] = [10, e] if e%10 == 0 else [e%10, int(e/10+1)*10]
print(da + db + dc + dd + de - 10 + min(na,nb,nc,nd,ne))