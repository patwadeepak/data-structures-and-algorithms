#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    ll n; cin >> n;
    ll mx = -1;
    vector<ll> a(n);
    for (ll i=0; i<n; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    vector<ll> b, c;
    for (ll i=0; i<n; i++) {
        if (a[i] == mx) {
            c.push_back(a[i]);
        } else {
            b.push_back(a[i]);
        }
    }

    if (b.size() <= 0 || c.size() <= 0) {
        cout << -1;
        return;
    }
    cout << b.size() << " " << c.size() << "\n";
    for(auto x : b) cout << x << " ";
    cout << "\n";
    for(auto x : c) cout << x << " ";
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
        cout << "\n";
    }
    return 0;
}