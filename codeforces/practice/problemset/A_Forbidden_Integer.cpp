#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define endl "\n"

void solve() {
    ll n, k, x; cin >> n >> k >> x;
    if (x != 1) {
        cout << "YES" << endl;
        cout << n << endl;
        for(ll i=0; i<n; i++) {
            cout << 1 << " ";
        }
        cout << endl;
    } else if (k == 1) {
        cout << "NO" << endl;
    } else if (k==2) {
        if (x == 1) {
            if (n%2 != 0 || n < 2) {
                cout << "NO" << endl;
            } else {
                cout << "YES" << endl;
                cout << n/2 << endl;
                for (ll i=0; i<n/2; i++) {
                    cout << 2 << " ";
                }
                cout << endl;
            }
        }
    } else if (k >= 3) {
        if (x == 1) {
            if (n < 2) {
                cout << "NO" << endl;
            }
            else if (n%2 == 0) {
                cout << "YES" << endl;
                cout << n/2 << endl;
                for (ll i=0; i<n/2; i++) {
                    cout << 2 << " ";
                }
                cout << endl;
            } else if (n%3 == 0){
                cout << "YES" << endl;
                cout << n/3 << endl;
                for (ll i=0; i<n/3; i++) {
                    cout << 3 << " ";
                }
                cout << endl;
            } else {
                ll rem = n-3;
                ll twos = rem/2;
                cout << "YES" << endl;
                cout << 1+twos << endl;
                cout << 3 << ' ';
                for (ll i=0; i<twos; i++) {
                    cout << 2 << ' ';
                }
                cout << endl;
            }
        }
    }
    return; 
}

int main () {
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
