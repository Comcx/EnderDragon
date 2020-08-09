impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let N = nums.len();
        if N == 0 {
            return false;
        }
        let mut rc: Vec<bool> = vec![false; N];
        let mut nearest: usize = N - 1;
        rc[N-1] = true;
        (1..N).rev().for_each(|i| {
            if nums[i] as usize + i >= nearest {
                nearest = i;
                rc[i] = true;
            }
        });
        rc[0]
    }
}
