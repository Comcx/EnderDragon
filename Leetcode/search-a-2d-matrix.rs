impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        fn of(m: &Vec<Vec<i32>>, i: usize) -> i32 {
            if m.len() == 0 {
                return 0;
            }
            let n = m[0].len();
            m[i/n][i%n]
        }
        if matrix.len() == 0 || matrix[0].len() == 0 {
            return false;
        }
        let M = matrix.len();
        let N = matrix[0].len();
        let mut i = 0 as i32;
        let mut j = (M * N - 1) as i32;
        while i <= j {
            let k = (i + j) as usize / 2;
            if of(&matrix, k) == target {
                return true;
            }
            if of(&matrix, k) > target {
                j = k as i32 - 1;
            }
            else {
                i = k as i32 + 1;
            }
        }
        false
    }
}
