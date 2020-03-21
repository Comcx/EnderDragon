class Solution {
public:
  int findTargetSumWays(vector<int>& nums, int S);
};

//f N 0 = 1
//f N _ = 0
//f i a = f (i+1) (a-xs(i)) + f (i+1) (a+xs(i))
int Solution::findTargetSumWays(vector<int>& nums, int S) {
  unordered_map<int, int> rc;
  rc[0] = 1;
  for(int n : nums) {
    unordered_map<int, int> f;
    for(auto a : rc) {
      int sum = a.first, cnt = a.second;
      f[sum + n] += cnt;
      f[sum - n] += cnt;
    }
    rc = f;
  }
  return rc[S];
}

