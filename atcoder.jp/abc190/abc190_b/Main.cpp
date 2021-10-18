#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,s,d,x,y,res=0;
  cin >> n >> s >> d;
  for(int i = 0; i <  n; i++){
   cin >> x >> y;
   if (x < s && y > d) res=1;
   if (res==1) break;
  }
  if (res==1) cout << "Yes" << endl;
  else cout << "No" << endl;
}