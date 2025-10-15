#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n; cin >> n;
    ll odds = 0;
    for (ll i=0; i<n; i++) {
        ll temp; cin >> temp;
        if (temp%2 == 1) odds++;
    }
    string s = odds%2==1 ? "NO" : "YES";
    cout << s << endl;
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
/*
2 = 1 + 1
2 = 2 + 0 make sure that even sum is more than 2 and if not check both values.

even = even + even, if there are 0, 4, 6, .... odds
even = odd + odd, if there are exactly 2 odds 
odd = odd + even, if there are 1 odd, 3 odds, 5 odds, ...... NO

*/