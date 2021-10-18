#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  long long max=0;
  long long ans=0;
  long long a[N];
  for (int i = 0; i < N; ++i) {
    cin >> a[i];
    if (a[i] > max ) {
      max = a[i];
    }
    else {
      ans = ans + (max - a[i]);
    }
  }  
  cout << ans << endl;
}