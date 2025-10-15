#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool check1(unordered_map<char, int>& f) {
        if (f.size() == 0)
            return true;
        
        int value = 0; 
        for (auto& v : f) {
            if (v.second != 0) {
                value = v.second;
                break;
            }
        }

        for (auto it = f.begin(); it != f.end(); it++) {
            if (it->second != 0 && value != it->second)
                return false;
        }
        return true;
    }

    int longestBalanced(string s) {
        int n = s.length();
        unordered_map<char, int> f;
        for (int i = 0; i < n; i++) {
            char temp = s[i];
            if (f[temp] > 0) {
                f[temp] += 1;
            } else {
                f[temp] = 1;
            }
        }

        int ml = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (i != n - 1)
                f[s[i + 1]] -= 1;

            unordered_map<char, int> f1(f);
            for (int j = 0; j < n - i; j++) {
                if (check1(f1)) {
                    ml = max(i + 1, ml);
                }
                if (i + j + 1 <= n - 1) {
                    f1[s[j]] -= 1;
                    f1[s[i + j + 1]] += 1;
                }
            }
        }
        return ml;
    }
};

int main() {
    Solution sol;
    string s = "abbac";
    int ans = sol.longestBalanced(s);
    cout << ans << '\n';
    return 0;
}
// Solved after contest