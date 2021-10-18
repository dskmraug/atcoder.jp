x = input()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
x4 = int(x[3])
bool = 0
if (x1 == x2 and x2 == x3 and x3 == x4): bool = 1
x21 = x2-x1
if x21 == -9 : x21 += 10
x32 = x3-x2
if x32 == -9 : x32 += 10
x43 = x4-x3
if x43 == -9 : x43 += 10
if (x21 ==1 and x32 == 1 and x43 == 1): bool = 1
print("Weak") if(bool) else print("Strong")