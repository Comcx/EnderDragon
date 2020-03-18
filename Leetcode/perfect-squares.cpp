class Solution {
public:
  int numSquares(int n);
};

//f 1 = 1
//f 0 = 0
//f n = foldl (\a i -> min a (1 + f (n-i*i))) 0 [1..sqrt n]
int Solution::numSquares(int n) {
  if(n <= 0) return 0;
  if(n == 1) return 1;
  
  vector<int> rc(n+1, INT_MAX);
  rc[0] = 0;
  for(int i(1); i <= n; ++i)
    for(int j(1); j <= (int)sqrt(i); ++j)
      rc[i] = min(rc[i], 1 + rc[i - j*j]);
  return rc[n];
}




