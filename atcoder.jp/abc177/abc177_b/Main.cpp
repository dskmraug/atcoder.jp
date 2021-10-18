#include <bits/stdc++.h>
using namespace std;
int main()
{
   string s,t;
   cin >> s >> t;
   int ns = s.size();
   int nt = t.size();
   int res;
   int min=2000;
   for(int i = 0; i < ns-nt+1; ++i) {
     res = 0;
     string sub = s.substr(i,nt);
     for (int j = 0; j < nt; ++j) {
       if(sub[j] != t[j]) res++;
     }
     if (res < min ) min = res;
     if (min ==0) break;
   }
   cout << min << endl;
}