s = [str(input()) for _ in range(4)]
bool = False
if (s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1): bool = True
print("Yes") if(bool) else print("No")