class Solution {
  vector<vector<int>> 
    twoSum(vector<int> &nums, int i, int j, int target) {
        
        if(nums.size() < 2) return {};
        
        vector<vector<int>> ans {};
        int I(i), J(j);
        while(i < j) {
            int sum = nums[i] + nums[j];
            if(sum == target) {
                ans.push_back({nums[i], nums[j]});
                while(i < J && nums[i+1] == nums[i]) ++i;
                while(j > I && nums[j-1] == nums[j]) --j;
                ++i, --j;
            }
            else if(sum < target) ++i;
            else --j;
        }
        return ans;
    }
    vector<vector<int>> 
    oneSum(vector<int> &nums, int i, int j, int target) {
        
        if(nums.size() < 1 || j - i < 0) return {};
        
        vector<vector<int>> ans {};
        for(int ii(i); ii <= j; ++ii) {
            if(nums[ii] == target) ans.push_back({nums[ii]});
            while(ii < j && nums[ii+1] == nums[ii]) ++ii;
            ++ii;
        }
        return ans;
    }
  
public:
    vector<vector<int>> 
    kSum(vector<int> &nums, int k, int i, int j, int target) {
        
        if(nums.size() < k || k == 0 || k < 1 || i > j) return {};
        if(k == 1) return oneSum(nums, i, j, target);
        if(k == 2) return twoSum(nums, i, j, target);
        
        vector<vector<int>> ans {};
        for(int ii(i); ii <= j - (k-1); ++ii) {
            
            int rest = target - nums[ii];
            auto res = kSum(nums, k-1, ii+1, j, rest);
            for(auto &v : res) {
                v.push_back(nums[ii]);
            }
            ans.insert(ans.end(), res.begin(), res.end());
            while(ii <= j - (k-1) && nums[ii+1] == nums[ii]) ++ii;
        }
        return ans;
    }
};




