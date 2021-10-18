#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }
  vector<vector<char>> res(N, vector<char>(N, '-'));
  
  for (int i = 0; i < M; i++) {
      A.at(i)--; B.at(i)--;
      res.at(A.at(i)).at(B.at(i)) = 'o';
      res.at(B.at(i)).at(A.at(i)) = 'x';
    }
   for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << res.at(i).at(j);
      if (j == N - 1) {
        cout << endl;  // 行末なら改行
      }
      else {
        cout << " ";  // 行末でないなら空白を出力
      }
    }
  }
}