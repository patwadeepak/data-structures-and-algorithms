#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

// submitted but got TLE in contest
void solve() {
    ll n, q; cin >> n >> q;
    string s; cin >> s;
    vector<ll> a(q);
    bool has_b = false;
    for (auto& ai : a) {
        cin >> ai;
        if (ai == 'B') {
            has_b = true;
        }
    }

    for (ll i=0; i<q; i++) {
        ll ops = 0;
        while (a[i] > 0) {
            char si = s[ops%n];
            if (si == 'A') {
                a[i]--;
            } else {
                a[i] /= 2;
            }
            ops++;
        }
        cout << ops << endl;
    }

    return;
}

// attempt after contest
void solve1() {
    ll n, q; cin >> n >> q;
    string s; cin >> s;
    vector<ll> a(q);
    vector<ll> ops(q, 0);
    for (auto& ai : a) {
        cin >> ai;
    }

    ll A = 0;
    ll B = 0;
    ll p = 0;
    ll q1 = 1;
    if (a[0] == 'A') {
        A++;
    } else {
        B++;
    }

    for (ll i=1; i<=n; i++) {
        if (i<n && s[i] == s[i-1]) {
            if (s[i] == 'A') A++;
            else B++;
        } else {
            if (s[i-1] == 'B') {
                q1 *= pow(2, B);
                B = 0;
                A = 1;
            } else {
                p += A*q1;
                A = 0;
                B = 1;
            }
        }
    }

    for (auto ai : a) {
        ll value = 0;
        ll x = ai;
        while (ai > p) {
            ll y = (ai - p)/q1;
            value += n;
            ai = y;
        }
        x = ai;
        while (x > 0) {
            for (auto si : s) {
                if (si == 'A') {
                    x--;
                } else {
                    x /= 2;
                }
                value++;
                if (x <= 0) {
                    break;
                }
            }
        }
        cout << value << endl;
    }
    return;
}

int main () {
    FASTIO;
    ll t; cin >> t;
    while (t--) {
        solve1();
    }
    return 0;
}
