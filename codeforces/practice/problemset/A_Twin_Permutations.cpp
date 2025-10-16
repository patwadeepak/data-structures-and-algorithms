#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, ai; cin >> n;
    for (ll i=0; i<n; i++) {
        cin >> ai;
        cout << n-ai+1 << ' ';
    }
    cout << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}