impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut n_0 = 0;
        let mut n_1 = 0;
        let mut n_2 = 0;
        for x in nums.iter() {
            match x {
                0 => {n_0 += 1;},
                1 => {n_1 += 1;},
                2 => {n_2 += 1;},
                _ => {}
            }
        }
        for i in 0..nums.len() {
            nums[i] = if n_0 > 0 {
                n_0 -= 1;
                0
            }
            else if n_1 > 0 {
                n_1 -= 1;
                1
            }
            else {
                2
            }
        }
    }
}
