#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void solve() {
    ll n, a, b; cin >> n >> a >> b;
    string s; cin >> s;

    // vector<ll> psa(n), psb(n);
    // psa[0] = s[0] == 'a' ? 1 : 0;
    // psb[0] = s[0] == 'b' ? 1 : 0;

    // for (ll i=1; i<n; i++) {
    //     psa[i] = psa[i-1] + (s[i] == 'a');
    //     psb[i] = psb[i-1] + (s[i] == 'b');
    // }

    ll cnt_a=0, cnt_b=0;
    ll l=0, r=0;
    ll ans = 0;
    while (l<=r && l<n && r<n) {
        if (s[r] == 'a') cnt_a++;
        else cnt_b++;

        if (cnt_a < a) {
            r++;
            continue;
        } 
        if (cnt_b >= b) {
            if (l+1<=r) {
                if (s[l] == 'a') cnt_a--;
                else cnt_b--;
                l++;
            } else {
                r++;
            }
            continue;
        }
        ans++;
        r++;
    }
    cout << ans << endl;
    return;
}

int main () {
    FASTIO;
    ll t = 1; // cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
