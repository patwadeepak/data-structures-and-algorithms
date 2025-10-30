#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    vector<ll> a(3);
    cin >> a[0] >> a[1] >> a[2];
    sort(a.begin(), a.end());
    ll n; cin >> n;
    ll i = 0;

    ll num = a[2];

    ll next01 = a[0];
    ll next02 = a[0];
    ll next12 = a[1];
    ll next10 = a[1];
    ll next20 = a[2];
    ll next21 = a[2];
    ll next_a;
    ll next_b;
    ll next_c;

    while (num<=1e18) {
        next_a = next01*next10;
        next_b = next02*next20;
        next_c = next12*next21;
        if (next_a < next_b && next_a < next_c) {
            num = next_a;
            next01 *= a[0];
            next10 *= a[1];
        } else if (next_b < next_a && next_b < next_c) {
            num = next_b;
            next02 *= a[0];
            next20 *= a[2];
        } else {
            num = next_c;
            next12 *= a[1];
            next21 *= a[2];
        }
        i++;
        if (i == n) {
            cout << num << endl;
            return;
        } 
    }
    cout << -1 << endl;
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
