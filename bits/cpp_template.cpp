#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    vector<ll> a(n);
    for (auto& ai : a) {
        cin >> ai;
    }

    for (auto& ai : a) {
        cout << ai << " ";
    }
    cout << endl;
    return;
}

int main () {
    FASTIO;
    ll t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
