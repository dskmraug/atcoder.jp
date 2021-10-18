#include <bits/stdc++.h>
using namespace std;
int func (int n) {
  int sum=0;
  while(n > 0) {
    sum += n%10;
    n /= 10;
  }
  return sum;
}
int main() {
  int n,a,b;
  cin >> n >> a >> b;
  int ans=0;
  for (int i=1; i <= n; i++) {
    if ((func(i) >= a) && (func(i) <= b)) ans +=i;
  }
  cout << ans << endl;
}