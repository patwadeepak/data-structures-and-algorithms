#include<bits/stdc++.h>
using namespace std;

#define endl "\n"
#define FASTIO ios::sync_with_stdio(0);cin.tie(0)

typedef long long ll;

void check(vector<char>& s) {
    vector<char> stack;
    for (auto ch : s) {
        while (!stack.empty() && ch == ')' && stack.back() == '(') {
            stack.pop_back();
        }
        stack.push_back(ch);
    }
    if (stack.empty()) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return;
}

void solve() {
    ll q; cin >> q;

    vector<char> s;

    ll query_type;
    char bracket;
    for (ll i=0; i<q; i++) {
        cin >> query_type;
        if (query_type == 1) {
            cin >> bracket;
            s.push_back(bracket);
        } else {
            s.pop_back();
        }
        check(s);
    }
    return;
}

int main () {
    FASTIO;
    solve();
    return 0;
}

/*
This was not that hard but still could not solve it in contest.
This code is incomplete.

Atcoder problems being easier than codeforces.
I was suppose to be able to solve A, B and C in atcoder beginner contest by now.

But to my surprise, my progress has slowed and I am making silly mistakes as well.
*/