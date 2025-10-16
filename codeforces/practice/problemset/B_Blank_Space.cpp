#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, bs=0, lbs=0, ai; cin >> n;
    for (ll i=0; i<n; i++) {
        cin >> ai;
        if (ai == 0) {
            bs += 1;
            lbs = max(bs, lbs);
        } else {
            bs = 0;
        }
    }

    cout << lbs << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}