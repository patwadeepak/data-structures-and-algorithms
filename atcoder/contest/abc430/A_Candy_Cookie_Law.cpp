#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll a, b, c, d; cin >> a >> b >> c >> d;
    bool violation = false;
    if (c >= a && d < b) {
        violation = true;
    }
    string ans = violation ? "Yes" : "No";
    cout << ans << endl;
    return;
}

int main () {
    FASTIO;
    ll t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
