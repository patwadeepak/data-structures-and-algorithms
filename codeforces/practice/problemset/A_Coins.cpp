#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, k; cin >> n >> k;
    string ans = "NO";
    if (n%2==0 || n%k==0 || k==1) {
        ans = "YES";
    } else {
        if (k%2 == 1) {
            ans = "YES";
        } else {
            ans = "NO";
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