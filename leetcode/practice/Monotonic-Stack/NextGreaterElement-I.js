// 496. Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/description/
var nextGreaterElement = function(nums1, nums2) {
   d = {};
   s = []; 
   nums2.forEach((item, index) => {
    while (s.length > 0 && s[s.length-1] < item) {
        a = s.pop();
        d[a] = item;
    }
    s.push(item);
   });
   return nums1.map(item => d?.[item] ?? -1);
};

console.log(nextGreaterElement([4,1,2], [1, 3, 4, 2]));