#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, m; cin >> n >> m;
    unordered_set<ll> a;
    ll total = 0;
    for (ll i=0; i<n; i++) {
        ll temp; cin >> temp;
        a.insert(temp);
        total += temp;
    }

    if (total >= m) {
        ll req = total - m;
        if (a.count(req) > 0) {
            cout << "Yes\n";
            return;
        }
    }
    cout << "No\n";
    return;
}

int main () {
    FASTIO;
    solve();
    return 0;
}
