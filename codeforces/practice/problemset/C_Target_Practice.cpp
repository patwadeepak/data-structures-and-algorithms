#include<bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while(t--) {
        int ans = 0;
        char temp;
        for (int i=0; i<10; i++) {
            for (int j=0; j<10; j++) {
                cin >> temp;
                if (temp == 'X') {
                    ans += 1 + min(min(9 - i, 9 - j), min(i, j));
                }
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
