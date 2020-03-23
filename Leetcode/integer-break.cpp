class Solution {
public:
  int integerBreak(int n);
};

//f 2 = 1
//f n | n < 2 = 0
//f n = max $ map (\i -> max (i * f (n-i)) (i * (n-i))) [1..(n-1)]
int Solution::integerBreak(int n) {
  if(n < 2) return 0;
  
  vector<int> rc(n+1, 0);
  rc[0] = 0;
  rc[1] = 0;
  rc[2] = 1;
  for(int i(3); i <= n; ++i)
    for(int j(1); j < i; ++j)
      rc[i] = max(max(rc[i], j * (i-j)), j * rc[i-j]);
  
  return rc[n];
}




