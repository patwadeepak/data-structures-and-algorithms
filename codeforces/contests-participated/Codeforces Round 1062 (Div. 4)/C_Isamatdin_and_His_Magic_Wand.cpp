#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    bool hasOdd = false, hasEven = false;
    vector<ll> a(n);
    for (auto& ai : a) {
        cin >> ai;
        if (ai%2 == 0) hasEven = true;
        else hasOdd = true;
    }

    if (hasEven && hasOdd) {
        sort(a.begin(), a.end());
    }

    for (auto& ai : a) {
        cout << ai << " ";
    }
    cout << endl;
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
