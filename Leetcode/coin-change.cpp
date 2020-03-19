class Solution {
public:
  int coinChange(vector<int>& coins, int amount);
};

//f 0 = 0
//f a = min $ map (\i -> 1 + f (a - i)) [1, 2, 5]
int Solution::coinChange(vector<int>& coins, int amount) {
  if(amount == 0)   return 0;
  if(coins.empty()) return -1;
  
  vector<int> rc(amount + 1, INT_MAX);
  rc[0] = 0;
  for(int i(1); i <= amount; ++i) {
    bool flag = false;
    for(int j(0); j < coins.size(); ++j) {
      if(i - coins[j] >= 0 && rc[i - coins[j]] != -1) {
        flag = true;
        rc[i] = min(rc[i], 1 + rc[i - coins[j]]);
      }
    }
    rc[i] = flag ? rc[i] : -1;
  }
  return rc[amount];
}

