#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int result = 2;
        int ans = 2;
        int n = nums.size();
        for (int i=2; i<n; i++) {
            if (nums[i] == nums[i-1]+nums[i-2]) {
                ++ans;
                result = max(result, ans);
            } else {
                ans = 2;
            }
        }

        return result;
    }
};
