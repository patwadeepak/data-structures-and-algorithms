#include<bits/stdc++.h>

using namespace std;

class Solution {
  public:
    int smallestSubWithSum(int x, vector<int>& arr) {
        int l=0, r=0, s=arr[0];
        int n = arr.size();
        int ans = n+1;
        while (l<=r && r<n) {
            if (s > x) {
                ans = min(ans, r-l+1);
                if (r == l) {
                    return 1;
                } else {
                    s -= arr[l];
                    l++;
                }
            } else {
                r++;
                if (r<n) {
                    s += arr[r];
                }
            }
        }
        return ans == n+1 ? 0 : ans;
    }
};

int main() {
    Solution s = Solution();
    vector<int> arr = {1, 4, 45, 6, 0, 19};
    int smallestSubsetLength = s.smallestSubWithSum(51, arr);
    cout << smallestSubsetLength << '\n';
    return 0;
}