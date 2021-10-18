#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  long long int L=s.size();
  long long sum=0;
  for (int i = 0; i < L; ++i) {
    int j = s[i] - '0';
    sum=sum+j;  
    }
  if (sum % 9 ==0) cout << "Yes" << endl;
  else cout << "No" << endl;
}