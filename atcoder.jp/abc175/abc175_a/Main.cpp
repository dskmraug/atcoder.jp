#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int cnt = 0;
    if (s[0]== 'R') ++cnt;
    if (s[1] == 'R') ++cnt;
    if (s[2] == 'R') ++cnt;
    if (s == "RSR")cnt=1;
    
    cout << cnt << endl;
}