
class Solution {
public:
  int singleNumber0(vector<int>& nums) {
    unordered_set<int> st;
    for(int num : nums) {
      if (st.count(num)) st.erase(num);
      else st.insert(num);
    }
    return *st.begin();
  }
  int singleNumber(vector<int>& nums) {
    int res = 0;
    for(auto num : nums) res ^= num;
    return res;
  }
};


