use std::collections::HashMap;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let xs = word1.as_bytes();
        let ys = word2.as_bytes();
        let mut rc = HashMap::new();
        fn min_dis<'a, 'b>(
            xs: &'a [u8], ys: &'b [u8],
            rc: &mut HashMap<(&'a [u8], &'b [u8]), i32>
        ) -> i32 {
            if xs.len() == 0 || ys.len() == 0 {
                return xs.len().max(ys.len()) as i32;
            }
            if let Some(cnt) = rc.get(&(xs, ys)) {
                return *cnt;
            }
            let ans = if xs[0] == ys[0] {
                min_dis(&xs[1..], &ys[1..], rc)
            }
            else {
                min_dis(&xs[1..], &ys[1..], rc)
                    .min(min_dis(&xs[1..], ys, rc))
                    .min(min_dis(xs, &ys[1..], rc)) + 1
            };
            rc.insert((xs, ys), ans);
            ans
        }
        min_dis(&xs, &ys, &mut rc)
    }
}
