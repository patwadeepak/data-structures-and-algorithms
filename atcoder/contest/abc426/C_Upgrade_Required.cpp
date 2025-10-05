// https://atcoder.jp/contests/abc426/tasks/abc426_c
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;
    vector<int> a(n+1, 1);
    int p = 1;
    while(q--){
        int x, y;
        cin >> x >> y;
        int u = 0;
        while(p <= x){
            u += a[p];
            a[p] = 0;
            p++;
        }
        a[y] += u;
        cout << u << '\n';
    }
    return 0;
}
