#include<bits/stdc++.h>
using namespace std;
int main() {
  int n, temp = 0; cin >> n;
  int ops = INT_MAX;
  for(int i=0; i<n; i++){
    cin >> temp;
    ops = min(abs(temp), ops);
  }
  cout << ops << '\n';
  return 0;
}