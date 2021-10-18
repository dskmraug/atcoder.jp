#include <bits/stdc++.h>
using namespace std;
 
int main() {
  long n, d, x, y, temp;
  int cnt;
  cin >> n >> d;
  cnt =0;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
        temp = x * x + y * y;
        if (temp <= d*d ) {
        cnt = cnt + 1;
    }
  }
  cout << cnt << endl;
}