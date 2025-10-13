#include<bits/stdc++.h>
using namespace std;
int main() {
    int a; cin >> a;
    string s; cin >> s;
    if (s[0] == 'B' || s[a-1] == 'A') {
        cout << "Yes" << '\n';
    } else {
        cout << "No" << '\n';
    }
    return 0;
}
/**
 * AXXXA - yes, AXXA -> ABBA, AABA, ABAA, AAAA
 * AXXXB
 * BXXXA
 * BXXXB
 * 
 * 
 * NOT SOLVED
 */
