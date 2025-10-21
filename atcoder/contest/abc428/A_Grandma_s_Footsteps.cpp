#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll s, a, b, x;
    cin >> s >> a >> b >> x;

    ll i = 0, d = 0;
    bool run = true;
    while (i<=x) {
        if (run) {
            if (i+a <= x) {
                i += a;
                d += a*s;
            } else {
                d += s*(x-i);
                break;
            }
        } else {
            i += b;
        }
        run = !run;
    }
    cout << d << endl;
    return;
}

int main () {
    FASTIO;
    // ll t; cin >> t;
    // while (t--) {
    solve();
    // }
    return 0;
}
