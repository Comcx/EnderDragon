impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        fn back(xs: &mut Vec<i32>, I: usize, step: usize) {
            for i in I..xs.len() {
                xs[i-step] = xs[i];
            }
        }
        if nums.len() == 0 {
            return 0;
        }
        let mut cnt = 1;
        let mut sum = 0;
        let mut pre = nums[0];
        let mut i = 1;
        let mut N = nums.len();
        while i < N {
            if nums[i] == pre {
                cnt += 1;
                i += 1;
                continue;
            }
            pre = nums[i];
            if cnt > 2 {
                back(nums, i, cnt - 2);
                i -= cnt - 2;
                N -= cnt - 2;
            }
            sum += if cnt > 2 {2} else {cnt};
            cnt = 1;
            i += 1;
        }
        (sum + if cnt > 2 {2} else {cnt}) as i32
    }
}
