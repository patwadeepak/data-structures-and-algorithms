#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, ans, twos = 0, temp; cin >> n;
    vector<ll> twos_idx;
    for (ll i=0; i<n; i++) {
        cin >> temp;
        if (temp == 2) {
            twos += 1;
            twos_idx.push_back(i);
        }
    }

    if (twos == 0) {
        ans = 1;
    } else if (twos%2 == 1){
        ans = -1;
    } else {
        ans = twos_idx[(ll)(twos/2)-1]+1;
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
