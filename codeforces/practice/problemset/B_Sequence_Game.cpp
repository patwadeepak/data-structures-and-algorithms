#include<bits/stdc++.h>
using namespace std;

vector<int> solve(vector<int>& a, int n) {
  vector<int> ans = {a[0]};
  for (int i=1; i<n; i++) {
    if (a[i-1] <= a[i]) {
      ans.push_back(a[i]);
    } else {
      ans.push_back(a[i]);
      ans.push_back(a[i]);
    }
  }
  return ans;
}

int main() {
  int t; cin >> t;
  while (t--) {
    int n; cin >> n;
    vector<int> a(n); for (auto& ai : a) { cin >> ai; }
    auto ans = solve(a, n);
    // print output
    cout << ans.size() << '\n';
    for (auto& ai : ans) { cout << ai << ' '; }
    cout << '\n';
  }
  return 0;
}
