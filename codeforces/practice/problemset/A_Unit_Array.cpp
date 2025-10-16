#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, s=0, p=1, ans=0, temp; cin >> n;
    for (ll i=0; i<n; i++) { cin >> temp; s += temp; p *= temp; }
    if (!(s >= 0 && p == 1)) {
        if (s<0) {
            ans += (ll)ceill(abs(s)/2.0);
        }
        if (p == -1) {
            if (ans%2 != 1) {
                ans += 1;
            }
        } else {
            if (ans%2 != 0) {
                ans += 1;
            }
        }
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