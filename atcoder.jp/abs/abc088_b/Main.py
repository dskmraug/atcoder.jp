n = int(input())
a = list(map(int,input().split()))
sa = 0
sb = 0
a_s = sorted(a,reverse=True)
sa=sum(a_s[0::2])
sb=sum(a_s[1::2])
print(sa-sb)