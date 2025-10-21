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
    ll t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}

/*
My approach was very dubious.
I got quite close but in contest
it did not feel like I was close to solving this at all.

Maybe because I have a mindset of fear and less experienced with XOR
and bit manipulation problems coupled with the fact that I thought
this was a div2 contest.

Anyway this whole contest was a bust for me.
*/ 