#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll a, b, c, d; cin >> a >> b >> c >> d;
    string possible = (a==b) && (a==c) && (a==d) ? "YES" : "NO";
    cout << possible << endl;
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
