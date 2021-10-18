#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A;
  cin >> A;
  if (A%1000 == 0) {
    cout << 0 << endl;
  }
  else {
    cout << 1000 - (A%1000) << endl;
  }
}