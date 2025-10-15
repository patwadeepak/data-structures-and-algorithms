#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n; cin >> n;
    vector<ll> a(n); for (auto& ai : a) { cin >> ai; }
    ll min_ops = LLONG_MAX;
    for (ll i=1; i<n; i++) {
        ll diff = a[i] - a[i-1];
        if (diff < 0) { min_ops = 0; break; }
        else if (diff == 0) { min_ops = 1; }
        else if (diff%2 == 0) {
            min_ops = min(min_ops, 1 + (ll)ceil(diff/2.0));
        } else {
            min_ops = min(min_ops, (ll)ceil(diff/2.0));
        }
    }
    cout << min_ops << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
