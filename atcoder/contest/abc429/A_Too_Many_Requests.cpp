#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, m; cin >> n >> m;
    for (ll i=1; i<=n; i++) {
        if (i<=m) {
            cout << "OK\n";
        } else {
            cout << "Too Many Requests\n";
        }
    }
    return;
}

int main () {
    FASTIO;
    solve();
    return 0;
}
