n = int(input())
ans = n / 1.08
bool = 0
if (int(int(ans) * 1.08) == n):
  bool = 1
if(int(int(ans+1) * 1.08) == n):
  bool = 2
print(int(ans)) if bool == 1 else print(int(ans+1)) if bool == 2 else print(":(")