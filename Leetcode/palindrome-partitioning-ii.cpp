
class Solution {
public:
  //f i = if isPalindrome (j+1) N then min (f j + 1)
  int minCut(string s) {
    if(s.empty()) return 0;
    
    int n = s.size();
    vector<vector<bool>> p(n, vector<bool>(n));
    vector<int> rc(n);
    for(int i(0); i < n; ++i) {
      rc[i] = i;
      for(int j(0); j <= i; ++j) {
        if (s[i] == s[j] && (i - j < 2 || p[j + 1][i - 1]))
          p[j][i] = true, 
          rc[i] = j == 0 ? 0 : min(rc[i], rc[j - 1] + 1); 
      }
    }
    return rc[n - 1];
  }
};



