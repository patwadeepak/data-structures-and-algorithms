#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, k; cin >> n >> k;
    string s; cin >> s;

    map<string, int> counts;
    int max_cnt = 0;

    for (ll i = 0; i <= n - k; i++) {
        string t = s.substr(i, k);
        counts[t]++;
        max_cnt = max(max_cnt, counts[t]);
    }

    set<string> strs;
    for (auto& pair : counts) {
        if (pair.second == max_cnt) {
            strs.insert(pair.first);
        }
    }
    
    cout << max_cnt << endl;
    for (auto& word : strs) {
        cout << word << ' ';
    }
    cout << endl;
}

int main () {
    FASTIO;
    solve();
    return 0;
}
