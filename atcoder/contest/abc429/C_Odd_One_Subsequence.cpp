#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    vector<ll> a(n);

    ll singles = 0;
    unordered_set<ll> multis;
    unordered_map<ll, ll> m;
    for (auto& ai : a) {
        cin >> ai;
        m[ai]++;
        if (m[ai] == 1) singles++;
        else if (m[ai] == 2) {
            singles--;
            multis.insert(ai);
        }
    }
    if (multis.size() == 0) {
        cout << 0 << endl;
        return;
    }

    if (m.size() == 1) {
        cout << 0 << endl;
        return;
    }

    ll ans = 0;
    for (auto& ai : multis) {
        ans += (m[ai]*(m[ai]-1)/2)*(singles + multis.size() - 1);
    }
    cout << ans << endl;
    return;
}

int main () {
    FASTIO;
    solve();
    return 0;
}
