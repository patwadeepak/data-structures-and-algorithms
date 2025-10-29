#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    set<ll> a;
    for (ll i=0; i<n; i++) {
        ll temp;
        cin >> temp;
        a.insert(temp);
    }

    ll k = 2;
    ll max_x = pow(10, 18);
    while (k<=max_x) {
        for (auto& ai : a) {
            if (gcd(ai, k) == 1) {
                cout << k << endl;
                return;
            };
        }
        k++;
    }
    cout << -1 << endl;
    return;
}

int main () {
    FASTIO;
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
