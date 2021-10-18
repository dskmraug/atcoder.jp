#include <bits/stdc++.h>
using namespace std;
int main() {
  bool ans = false;
  int N;
  cin >> N;
  int x[N],y[N];
  double mx=-1.0;
  for (int i = 0; i < N; ++i) {
    cin >> x[i] >> y[i];
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
        double d = pow(pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2),0.5);
        mx = max(mx,d);
    }
  }
  cout << setprecision(8) << mx << endl;
}