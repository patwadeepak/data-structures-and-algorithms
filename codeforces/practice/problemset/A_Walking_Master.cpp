#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll a, b, c, d; cin >> a >> b >> c >> d;
    c -= a;
    d -= b;
    ll ans;
    if (d < 0) {
        ans = -1;
    } else if (c != 0 && d/(double)c < 1 && d/(double)c > 0) {
        ans = -1;
    } else if (d/(double)c == 0) {
        if (c <= 0) {
            ans = abs(c);
        } else {
            ans = -1;
        }
    } else {
        ans = abs(c-d) + d;
    }
    cout << ans << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
