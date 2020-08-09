impl Solution {
    pub fn spiral(matrix: &Vec<Vec<i32>>) -> Vec<i32> {
        fn shape(m: &Vec<Vec<i32>>) -> (usize, usize) {
            if m.len() == 0 {
                (0, 0)
            }
            else {
                (m.len(), m[0].len())
            }
        }
        let (row, col) = shape(matrix);
        if row == 0 || col == 0 {
            return vec![];
        }
        if row == 1 {
            return matrix[0].clone();
        }
        if col == 1 {
            let mut ans = Vec::new();
            matrix.iter().for_each(|v| ans.push(v[0]));
            return ans;
        }
        /*      a
           d         b
                c
        */
        let a = matrix[0].clone();
        let b = matrix[1..row-1].iter()
          .map(|v| *v.last().unwrap()).collect::<Vec<_>>();
        let mut c = matrix.last().unwrap().clone();
        let mut d = matrix[1..row-1].iter().map(|v| v[0]).collect::<Vec<_>>();
        c.reverse();
        d.reverse();
        let v: Vec<i32> = a.into_iter()
          .chain(b.into_iter())
          .chain(c.into_iter())
          .chain(d.into_iter()).collect();

        let m_rest: Vec<Vec<i32>> =
          matrix[1..row-1].iter().map(|v|
              v[1..v.len()-1].iter().cloned().collect()).collect();

        let rest = Solution::spiral(&m_rest);
        v.into_iter().chain(rest.into_iter()).collect()
    }
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        Solution::spiral(&matrix)
    }
}
