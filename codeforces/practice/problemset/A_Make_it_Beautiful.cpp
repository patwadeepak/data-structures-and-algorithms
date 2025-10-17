#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, s=0;
    unordered_map<ll, ll> cnt;
    bool beautiful = true;
    cin >> n;
    vector<ll> a(n);
    for (auto& ai : a) {
        cin >> ai;
        if (s == ai) {
            beautiful = false;
        }
        s += ai;
        if (cnt.count(ai) > 0) cnt[ai] += 1;
        else cnt[ai] = 1;
    }

    if (beautiful) {
        cout << "YES" << endl;
        for (auto& ai : a) {
            cout << ai << " ";
        }
        return;
    }

    if ((n == 2 && a[0] == a[1]) || cnt.size() == 1) {
        cout << "NO" << endl;
        return;
    }

    ll r = n-1;
    while (r>=0) {
        if (a[r] == a[n-1]) {
            r--;
        } else {
            break;
        }
    }

    cout << "YES" << endl;
    cout << a[n-1] <<' '<< a[r] <<' ';

    for (ll i=n-2; i>=0; i--) {
        if (r == i) continue;
        cout << a[i] << " ";
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
