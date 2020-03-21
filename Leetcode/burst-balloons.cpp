class Solution {
public:
  int maxCoins_mem(vector<int>& nums);
  int maxCoins(vector<int>& nums);
};

//This problem is interesting that
//We need to divide the array by the last balloon in order to
//get 2 independent subproblems.
int DP(int i, int j, const vector<int> &nums, vector<vector<int>> &dp) {
  if(dp[i][j] > 0) return dp[i][j];
  for(int x = i; x <= j; x++) {
    int cur = DP(i, x - 1, nums, dp) + 
      nums[i - 1] * nums[x] * nums[j + 1] + DP(x + 1, j, nums, dp);
    if (cur > dp[i][j]) dp[i][j] = cur;
  }
  return dp[i][j];
}
//Memory method
int Solution::maxCoins_mem(vector<int>& nums) {
  int n = nums.size();
  nums.insert(nums.begin(), 1);
  nums.insert(nums.end(),   1);
  vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
  return DP(1, n, nums, dp);
}


//DP method
int Solution::maxCoins(vector<int>& nums) {
  vector<int> arr;
  arr.push_back(1);
  for(int i(0); i < nums.size(); i++){
    arr.push_back(nums[i]);
  }
  arr.push_back(1);
  int n = nums.size();
  vector<vector<int>> dp(n+2, vector<int>(n+2));
  for(int l(3); l <= n+2; l++)
    for(int i(0); i <= n+2-l; i++)
      for(int j(i+1); j < i+l-1; j++)
	dp[i][i+l-1] =
	  max(dp[i][i+l-1], arr[i]*arr[i+l-1]*arr[j]+dp[i][j]+dp[j][i+l-1]);

  return dp[0][n+1];
}




