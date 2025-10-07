#include<bits/stdc++.h>
#define ll long long int

using namespace std;

class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        ll x = 0;
        sort(nums.begin(), nums.end());
        ll last_non_zero_index = -1;
        for (ll i=0; i<nums.size(); i++) {
            x ^= nums[i];
            if (x!=0) {
                last_non_zero_index = i;
            }
        }

        return last_non_zero_index + 1;
    }
};
