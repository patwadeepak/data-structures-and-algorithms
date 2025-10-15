#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n; cin >> n;
    vector<ll> a(n); for (auto& ai : a) { cin >> ai; }
    for (auto& ai : a) { cout << ai << " "; } cout << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}