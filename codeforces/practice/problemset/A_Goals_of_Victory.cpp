#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--) {
        int n, sum=0, temp;
        cin >> n;
        for (int i=0; i<n-1; i++) {
            cin >> temp;
            sum += temp;
        }
        cout << -1*sum << '\n';
    }
    
    return 0;
}
