impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn sets(xs: &[i32]) -> Vec<Vec<i32>> {
            if xs.len() == 0 {
                return vec![vec![]];
            }
            let subs = sets(&xs[1..]);
            let mut news = subs.clone();
            for i in 0..news.len() {
                news[i].push(xs[0]);
            }
            subs.into_iter().chain(news.into_iter()).collect()
        }
        sets(&nums)
    }
}
