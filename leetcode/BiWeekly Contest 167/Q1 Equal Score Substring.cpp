#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool scoreBalance(string s) {
        int n = s.length();
        vector<int> ps(n);
        int sum = 0;

        for (int i = 0; i<n; i++) {
            sum += s[i]-'a'+1;
            ps[i] = sum;
        }

        if (sum%2 != 0) {
            return false;
        }

        int half_sum = sum/2;
        for (int i = 0; i<n; i++) {
            if (half_sum == ps[i]) return true;
        }

        return false;
    }
};
