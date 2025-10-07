#include<bits/stdc++.h>
#define ll long long int

using namespace std;

class Solution {
public:
    string removeSubstring(string s, int k) {
        string st;

        const string open_pattern_str(k, '(');
        const string_view open_pattern(open_pattern_str);
        
        const string close_pattern_str(k, ')');
        const string_view close_pattern(close_pattern_str);

        for (char c : s) {
            st.push_back(c);

            if (st.length() >= static_cast<size_t>(2 * k)) {
                
                string_view last_k(st.data() + st.length() - k, k);
                string_view prev_k(st.data() + st.length() - 2 * k, k);

                if (last_k == close_pattern && prev_k == open_pattern) {
                    st.resize(st.length() - 2 * k);
                }
            }
        }
        
        return st;
    }
};
// The same solution was TLE in python but gott AC in C++