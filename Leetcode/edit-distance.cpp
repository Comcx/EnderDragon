

class Solution {
public:
  int minDistance0(string word1, string word2);
  int minDistance1(string word1, string word2);
};

// f(i, j) = 
//   min(f(i+1, j+1), f(i, j+1), f(i+1, j) + if(a(i) == b(i)) 0 else 1)
// f(I, J) = 0
// f(i, J) = I - i
// f(I, j) = J - j
int Solution::minDistance0(string word1, string word2) {
  int I = word1.size();
  int J = word2.size();
  vector<vector<int>> rc(I+1, vector<int>(J+1, 0));
  
  for(int i(0); i < I; ++i) rc[i][J] = I - i;
  for(int j(0); j < J; ++j) rc[I][j] = J - j;
  for(int i(I-1); i >= 0; --i) 
    for(int j(J-1); j >= 0; --j) 
      rc[i][j] = 
        min(min(rc[i+1][j] + 1, rc[i][j+1] + 1), 
                rc[i+1][j+1] + (word1[i] == word2[j] ? 0 : 1));
  
  return rc[0][0];
}


int Solution::minDistance1(string word1, string word2) {
  
  int m = word1.size(), n = word2.size();
  int rc[m + 1][n + 1];
  for(int i(0); i <= m; ++i) rc[i][0] = i;
  for(int j(0); j <= n; ++j) rc[0][j] = j;
  
  for(int i(1); i <= m; ++i)
    for(int j(1); j <= n; ++j)
      rc[i][j] = min(min(rc[i-1][j] + 1, rc[i][j-1] + 1),
                     rc[i-1][j-1] + (word1[i-1] == word2[j-1] ? 0 : 1));
  
  return rc[m][n];
}


