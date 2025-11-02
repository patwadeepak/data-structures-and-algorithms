#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    char temp;
    ll n, m; cin >> n >> m;
    vector<vector<char>> a(n, vector<char>(n));
    unordered_set<string> my_set;
    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            cin >> temp;
            a[i][j] = temp;
        }
    }

    if (m == n) {
        cout << 1 << endl;
        return;
    }

    for (int i = 0; i<n-m+1; i++) {
        for (int j = 0; j<n-m+1; j++) {
            string p(m*m, '\0');
            int x = 0;
            for (int k = i; k<m+i; k++) {
                for (int l = j; l<m+j; l++) {
                    p[x] = a[k][l];
                    x++;
                }
            }
            my_set.insert(p);
        }
    }

    cout << my_set.size() << endl;
    return;
}

int main () {
    FASTIO;
    ll t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
