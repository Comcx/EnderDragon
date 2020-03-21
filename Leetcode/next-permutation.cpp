class Solution {
public:
  void nextPermutation(vector<int>& nums);
};

void Solution::nextPermutation(vector<int>& nums) {
  next_permutation(nums.begin(), nums.end());
}



