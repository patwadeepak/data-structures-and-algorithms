#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    ll a, b, c; cin >> a >> b >> c;
    ll p1 = ceil(c/2.0);
    ll p2 = c - p1;

    p1 += a;
    p2 += b;

    string s = (p1 > p2) ? "First" : "Second";
    cout << s << "\n";
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
