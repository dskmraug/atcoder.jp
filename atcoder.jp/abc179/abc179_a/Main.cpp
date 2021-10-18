#include <bits/stdc++.h> 

using namespace std; 

int main() { 

  string n; 

  cin >> n;
  char lastChar = n.at( n.length() - 1 ); 
  if (lastChar == 's' ) cout << n + "es" << endl;
  else cout << n + "s" << endl;

} 