
class Solution {
public:
  //f I J K = True
  //f i j K = False
  //f I J k = False
  //f I j k = if c[k] == b[j] then f I (j+1) (k+1) else False
  //f i J k = if c[k] == a[i] then f (i+1) J (k+1) else False
  //f i j k = (if c[k] == a[i] then f (i+1) j (k+1) else False)
  //       || (if c[k] == b[j] then f i (j+1) (k+1) else False)
  
  bool isInterleave(string s1, string s2, string s3) {
    int I = s1.size(), J = s2.size(), K = s3.size();
    vector<vector<vector<int>>> 
      rc(I+1, vector<vector<int>>(J+1, vector<int>(K+1, 0)));
    for(int i(I); i >= 0; --i) {
      for(int j(J); j >= 0; --j) {
        for(int k(K); k >= 0; --k) {
          if(i == I && j == J && k == K) rc[i][j][k] = true;
          else if(i == I && j == J) rc[i][j][k] = false;
          else if(i == I && k != K) rc[i][j][k] = s3[k] == s2[j] ? rc[I][j+1][k+1] : false;
          else if(j == J && k != K) rc[i][j][k] = s3[k] == s1[i] ? rc[i+1][J][k+1] : false;
          else if(k == K) rc[i][j][k] = false;
          else rc[i][j][k] = 
            (s3[k] == s1[i] ? rc[i+1][j][k+1] : false) ||
            (s3[k] == s2[j] ? rc[i][j+1][k+1] : false) ;
        }
      }
    }
    return rc[0][0][0];
  }
};




