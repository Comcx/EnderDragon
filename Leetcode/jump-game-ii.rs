impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let N = nums.len();
        if N == 0 {
            return 0;
        }
        let mut rc: Vec<i32> = vec![0; N];
        for i in (0..N-1).rev() {
            let mut min_steps = -1;
            (1..(nums[i] as usize).min(N-i-1) + 1).for_each(|j| {
                if rc[i+j] != -1 {
                    let steps = rc[i+j] + 1;
                    if (min_steps == -1 || steps < min_steps) {
                        min_steps = steps;
                    }
                }
            });
            rc[i] = min_steps;
        }
        rc[0]
    }
}
