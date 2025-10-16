#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    vector<ll> a(n);
    for (auto& ai : a) {
        cin >> ai;
    }

    string ans = "No";
    for (ll i=0; i<n-1; i++) {
        for (ll j=i+1; j<n; j++) {
            if (gcd(a[i], a[j]) <= 2) {
                ans = "Yes";
                break;
            }
        }
    }

    cout << ans << endl;
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
