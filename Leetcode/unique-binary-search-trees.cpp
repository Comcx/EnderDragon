class Solution {
public:
  int numTrees(int n);
};

//f 0 = 1
//f i = foldl (\e -> f (e-1) * f (i-e)) 0 [1..i]
int Solution::numTrees(int n) {
  vector<int> rc(n + 1, 0);
  rc[0] = rc[1] = 1;
  for(int i(2); i <= n; ++i) 
    for(int j(1); j <= i; ++j) rc[i] += rc[j-1] * rc[i-j];
  return rc[n];
}




