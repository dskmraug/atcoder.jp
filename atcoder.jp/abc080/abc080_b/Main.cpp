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
  int n;
  cin >> n;
  if (n%(func(n)) == 0) cout << "Yes" << endl;
  else cout << "No" << endl;
}