impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if intervals.len() == 0 {
            return vec![];
        }
        let mut xs = intervals.clone();
        xs.sort_by(|a, b| a[0].partial_cmp(&b[0]).unwrap());

        let mut res: Vec<Vec<i32>> = vec![];
        let mut prev = vec![xs[0][0], xs[0][0]];
        for v in xs.iter() {
            if v[0] <= prev[1] {
                prev = vec![prev[0], v[1].max(prev[1])];
                continue;
            }
            res.push(prev);
            prev = v.clone();
        }
        res.push(prev);
        res
    }
}
