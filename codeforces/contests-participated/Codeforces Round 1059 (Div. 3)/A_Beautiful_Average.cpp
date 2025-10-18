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

    ll maxA = -1;
    for (ll l=0; l<n; l++) {
        ll total = 0;
        for (ll r=l; r<n; r++) {
            total += a[r];
            maxA = max(maxA, total/(r-l+1));
        }
    }
    cout << maxA << endl;
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
I know that I missed the main point of the problem
when I solved it with this solution. But it was not my
day. I could not think straight and was looking to get any
solution to get AC. I looked at the time limit and
figured a O(n^2) solution would actually not get TLE.

So, I simply went ahead with it.

The real solution is just the max value in array because
adding any smaller value to it would decrease the avg.
*/