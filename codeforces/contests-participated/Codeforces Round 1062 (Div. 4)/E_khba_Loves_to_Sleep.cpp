#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, k, x; cin >> n >> k >> x;
    vector<ll> a(n);
    for (auto& ai : a) {
        cin >> ai;
    }

    sort(a.begin(), a.end());

    ll j = 0;
    map<ll, vector<ll>> si_map;
    for (ll i=0; i<=x; i++) {
        ll d = 0;
        if (a[i] <= a[j]) {
            d = a[j] - a[i];
        } else {
            if (j+1 <= x && abs(a[i]-a[j]) >= abs(a[i]-a[j+1])) {
                j++;
            }
            d = abs(a[j] - a[i]);
        }
        if (si_map.count(d)) {
            si_map[d].push_back(i);
        } else {
            si_map[d] = {i};
        }
    }

    for (auto it=si_map.rbegin(); it!=si_map.rend(); it++) {
        auto arr = it->second;
        for (auto arri : arr) {
            cout << arri << ' ';
            k--;
            if (k==0) break;
        }
        if (k==0) break;
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
