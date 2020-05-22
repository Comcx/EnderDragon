class Solution {
public:
  void check(vector<vector<char>>& board, 
             vector<vector<bool>>& rc, int i, int j) {
    if(i == board.size()   || j == board[0].size() ||
       i == -1  || j == -1 || 
       rc[i][j] || board[i][j] == 'X') return;
    
    rc[i][j] = true;
    check(board, rc, i-1, j);
    check(board, rc, i+1, j);
    check(board, rc, i, j-1);
    check(board, rc, i, j+1);
  }
  void solve(vector<vector<char>>& board) {
    if(board.empty()) return;
    
    int M(board.size()), N(board[0].size());
    vector<vector<bool>> rc(M, vector<bool>(N, false));
    for(int i(0); i < M; ++i)
      check(board, rc, i, 0),
      check(board, rc, i, N-1);
    
    for(int j(0); j < N; ++j)
      check(board, rc, 0, j),
      check(board, rc, M-1, j);
    
    for(int i(1); i < M-1; ++i)
      for(int j(1); j < N-1; ++j)
        if(!rc[i][j] && board[i][j] == 'O') board[i][j] = 'X';
  }
};

