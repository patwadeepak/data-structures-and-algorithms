#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n; cin >> n;
    string s;
    cin >> s;

    bool is_palindrome = true;
    ll pl1 = 0;
    ll pr1 = n-1;
    while (pl1>=0 && pl1<n && pr1>=0 && pr1<n && pl1 <= pr1) {
        if (s[pl1] == s[pr1]) {
            pl1++;
            pr1--;
            continue;
        }
        is_palindrome = false;
        break;
    }
    if (is_palindrome) {
        cout << 0 << endl << endl;
        return;
    }

    for (ll w=1; w<=n; w++) {
        for (ll l=0; l<=n; l++) {
            ll r = l+w-1;
            bool okay = true;
            for (ll i=l; i<r; i++) {
                if (s[i+1] == '0') {
                    if (s[i] == '0') continue;
                    else {
                        okay = false;
                        break;
                    }
                }
            }
            if (!okay) break;
            bool is_palin = true;
            ll pl = l == 0 ? r+1 : 0;
            ll pr = r == n-1 ? l-1 : n-1;
            while (pl>=0 && pl<n && pr>=0 && pr<n && pl <= pr) {
                if (s[pl] == s[pr]) {
                    pl++;
                    pr--;
                    if (pl == l) pl = r+1;
                    if (pr == r) pr = l-1;
                    continue;
                }
                is_palin = false;
                break;
            }
            if (is_palin) {
                cout << r-l+1 << endl;
                for (ll i=l; i<=r; i++) {
                    cout << i+1 << ' ';
                }
                cout << endl;
                return;
            }
        }
    }
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

/*
I did not read the problem correctly. 
I thought subarray instead of subsequence.
And this was a big blunder since I knew
the difference between subarray and subsequence very clearly.
*/