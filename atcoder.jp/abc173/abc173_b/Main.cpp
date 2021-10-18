#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  string s;
  int N_AC=0;
  int N_WA=0;
  int N_TLE=0;
  int N_RE=0;
	for (int i = 0; i < N; i++) {
		cin >> s;
        if (s=="AC") N_AC++;
        else if (s=="WA") N_WA++;
        else if (s=="TLE") N_TLE++;
        else if (s=="RE") N_RE++;
	}
cout << "AC x " << N_AC << endl;
cout << "WA x " << N_WA << endl;
cout << "TLE x " << N_TLE << endl;
cout << "RE x " << N_RE << endl;
}