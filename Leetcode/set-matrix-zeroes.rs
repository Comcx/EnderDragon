impl Solution {
    /*
    UNDERWORK!
    Need a better version with constant space.
    */
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        fn set_row(m: &mut Vec<Vec<i32>>, i: usize) {
            m[i] = vec![0; m[0].len()];
        }
        fn set_col(m: &mut Vec<Vec<i32>>, j: usize) {
            for i in 0..m.len() {
                m[i][j] = 0;
            }
        }
        if matrix.len() == 0 {
            return;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        let mut rc_row = vec![false; m];
        let mut rc_col = vec![false; n];
        for i in 0..m {
            for j in 0..n {
                if matrix[i][j] == 0 {
                    if !rc_row[i] {
                        rc_row[i] = true;
                    }
                    if !rc_col[j] {
                        rc_col[j] = true;
                    }
                }
            }
        }
        for i in 0..m {
            if rc_row[i] {
                set_row(matrix, i);
            }
        }
        for j in 0..n {
            if rc_col[j] {
                set_col(matrix, j);
            }
        }
    }
}
