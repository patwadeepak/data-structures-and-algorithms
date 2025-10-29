#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    string s, t;
    cin >> s >> t;

    unordered_map<char, ll> m;
    for (ll i=0; i<n; i++) {
        if (m.count(s[i])) m[s[i]]++;
        else m.insert({s[i], 1});
    }

    string ans = "YES";
    for (ll i=0; i<n; i++) {
        if (m[t[i]] > 0) m[t[i]]--;
        else {
            ans = "NO";
            break;
        };
    }

    cout << ans << endl;
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
