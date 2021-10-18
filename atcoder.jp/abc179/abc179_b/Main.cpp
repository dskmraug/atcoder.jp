#include <bits/stdc++.h> 

using namespace std; 

int main() { 

  int n;
  int cnt=0;
  int cnt_max=0;
  cin >> n;
  int d[n][2];
  for (int i = 0; i < n; ++i) {
  cin >> d[i][0] >> d[i][1];
    if (d[i][0] == d[i][1]) cnt++;
    else cnt =0;
    if (cnt > cnt_max) cnt_max = cnt;
    
  }
  if (cnt_max >= 3) cout << "Yes" << endl;
  else cout << "No" << endl;
} 