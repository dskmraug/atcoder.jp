#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N,K,x;
  int sum = 0;
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
     cin >> x;
    if (x <= K-x ) sum += x * 2;
    else sum += ((K-x) *2);
  }
  cout << sum << endl;  
}