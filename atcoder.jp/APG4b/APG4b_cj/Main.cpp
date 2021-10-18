#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  vector<int> test(N);
  int ave=0;
  for (int i = 0; i < N; i++) {
    cin >> test.at(i);
    ave += test.at(i);
  }
  ave /= N;
    for (int i = 0; i < N; i++) {
      if (test.at(i) >= ave) test.at(i) = test.at(i) - ave; 
      else test.at(i) = ave - test.at(i);
      cout << test.at(i) << endl;
  }
}