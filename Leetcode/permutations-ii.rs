use std::collections::HashSet;

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn dfs(nums: &mut Vec<i32>, begin: usize, res: &mut HashSet<Vec<i32>>) {
            if begin == nums.len() {
                res.insert(nums.clone());
                return;
            }
            for i in begin..nums.len() {
                nums.swap(begin, i);
                dfs(nums, begin + 1, res);
                nums.swap(begin, i);
            }
        }
        let mut ns = nums.clone();
        let mut res = HashSet::new();
        dfs(&mut ns, 0, &mut res);
        res.into_iter().collect::<Vec<Vec<_>>>()
    }
}
