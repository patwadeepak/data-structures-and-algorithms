#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, x=-1, ai; cin >> n;
    for (ll i=0; i<n; i++) {
        cin >> ai;
        if (x == -1) {
            x = ai;
        } else {
            x = x ^ ai;
        }
    }
    if (x==0 || n%2==1) {
        cout << x << endl;
    } else {
        cout << -1 << endl;
    }
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