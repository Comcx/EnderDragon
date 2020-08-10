impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = nums.len() - 1;
        while i < j {
            let k = (i + j) / 2;
            if nums[k] < nums[j] {
                j = k;
            }
            else if nums[k] > nums[j] {
                i = k + 1;
            }
        }
        nums[i]
    }
}
