#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, A, B, ans;
  string op;
  cin >> N >> A;
  ans = A;
  for (int i = 0; i < N; i++) {
    cin >> op >> B;
    if (op == "+")  ans += B;
    else if (op == "-") ans -=B;
    else if (op == "*") ans *=B;
    else if (op == "/") {
       if (B == 0) {
         cout << "error" << endl;
         break;
       }
       else  {
         ans /=B;
       }
    }
    else cout << "error" << endl;
  cout << i + 1 << ":" << ans << endl;
  }
}