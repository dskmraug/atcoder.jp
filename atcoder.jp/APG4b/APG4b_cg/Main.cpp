#include <bits/stdc++.h>
using namespace std;
 
int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }
  bool b = 0;
  for (int i=0; i<4; i++)
  if (data.at(i) == data.at(i+1)) {
    b = 1;
    break;
  }
  if(b)  cout << "YES" << endl;
  else cout << "NO" << endl;
}