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

    ll mx = a[0];
    bool flag = true;
    ll ops = 0;
    for (ll i=1; i<n; i++) {
        if (flag) {
            if (a[i-1] >= a[i]) {
                a[i] = mx;
                if (a[i-1] >= a[i]) {
                    ops += a[i-1] - a[i] + 1;
                }
            }
        } else {
            if (a[i-1] <= a[i]) {
                
            }
        }
        flag = !flag;
    }
    cout << endl;
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
