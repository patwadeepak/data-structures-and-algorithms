#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    string s; cin >> s;
    ll l=0, r=n-1, added = 0;
    while (l < r) {
        if ((s[l] == '1' && s[r] == '0') || (s[l] == '0' && s[r] == '1')) {
            added += 2;
        } else {
            break;
        }
        l++;
        r--;
    }
    cout << n-added << endl;
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