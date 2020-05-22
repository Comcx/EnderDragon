
//I'm too lazy that I don't want to implement dp...
class Solution {
public:
  vector<string> generate(int n, int a) {
    if(n == 0) return a == 0 ? vector<string>{""} : vector<string>{};
    if(a == 0) {
      vector<string> next = generate(n - 1, a + 1);
      for(string& s : next) s = "(" + s;
      return next;
    }
    vector<string> ans {};
    for(string s : generate(n - 1, a + 1)) ans.push_back("(" + s);
    for(string s : generate(n - 1, a - 1)) ans.push_back(")" + s);
    return ans;
  }
  vector<string> generateParenthesis(int n) {
    return generate(n * 2, 0);
  }
};




