#include <bits/stdc++.h>
using namespace std;

int main() {
  int a,b,c,tmp=0,res=0;
  cin >> a >> b >> c;
  tmp = a - b;
  if (tmp > 0) res=0;
  else if (tmp < 0) res=1;
  else if (tmp == 0) {
    if (c==1) res=0;
    else res=1;
  }
  if (res==0) cout << "Takahashi" << endl;
  else cout << "Aoki" << endl;
}