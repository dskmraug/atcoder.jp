#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  int flag = 0;
  string s;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> s;
    if (s == "Y")  {
      flag = 1;
      break;
    }
  }
  if (flag == 1) cout << "Four" << endl;
  else cout << "Three" << endl;
}