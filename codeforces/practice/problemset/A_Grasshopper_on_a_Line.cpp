#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, k; cin >> n >> k;
    if (n%k != 0) {
        cout << 1 << endl << n << endl;
        return;
    }
    ll i = 1;
    while (i<n) {
        if ((n-i)%k != 0 && i%k != 0) {
            cout << 2 << endl << n-i << ' ' << i << endl;
            return;;
        }
        i++;
    }
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
