#include <bits/stdc++.h>
using namespace std;
 
int main() {
  string str;
  int plus=0;
  int minus=0;
  cin >> str;
  for (int i = 0; i < str.size(); i++) {
    if (str.at(i) == '+') {
      plus++;
    }
    else if (str.at(i) == '-') {
      minus++;
    }
  
  }
 
  cout << 1 + plus - minus << endl;
}