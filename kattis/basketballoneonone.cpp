// https://open.kattis.com/problems/basketballoneonone
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a = 0;
    int b = 0;
    
    char last, x;
    while (cin >> x) {
        if (x == 'A' || x == 'B') {
            last = x;
        } else {
            if (last == 'A') {
                a += x - '0';
            } else {
                b += x - '0';
            }
        }
    }
    if (a > b) cout << 'A';
    else cout << 'B';
    return 0;
}
