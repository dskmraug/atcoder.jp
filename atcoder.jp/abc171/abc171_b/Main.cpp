#include <bits/stdc++.h>
using namespace std;
int main(){
  int N;
  int K;
  int ans = 0;
  cin >> N;
  cin >> K;  
  long long P[N];
  for(int i=0;i<N;i++){
    cin >> P[i];
  }
  sort(P, P + N);
  for(int i=0;i<K;i++){
    ans = ans + P[i];
  }  
  cout << ans << endl;
}