impl Solution {
    fn scan(height: &[i32]) -> (i32, i32, usize) {
        let mut water_cur = 0;
        let mut water_sum = 0;
        let mut left = 0;
        let mut i_left = 0;
        let mut i = 0;
        while i < height.len() {
            if height[i] >= left {
                water_sum += water_cur;
                water_cur = 0;
                left = height[i];
                i_left = i;
            }
            else {
                water_cur += left - height[i];
            }
            i += 1;
        }
        (water_sum, water_cur, i_left)
    }
    pub fn trap(height: Vec<i32>) -> i32 {
        let (mut water_sum, mut water_cur, i) = Solution::scan(&height);
        if water_cur > 0 {
            let mut heights = height.clone();
            let hs = &mut heights[i..];
            hs.reverse();
            water_sum += Solution::scan(hs).0;
        }
        water_sum
    }
}
