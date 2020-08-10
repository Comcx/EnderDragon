impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let deltas: Vec<i32> = gas.iter().zip(cost.iter()).map(|(g, c)| g - c).collect();
        if deltas.iter().sum::<i32>() < 0 {
            return -1;
        }
        let mut start = 0;
        let mut total = 0;
        deltas.iter().enumerate().for_each(|(i, d)| {
            total += d;
            if total < 0 {
                start = i + 1; //We can safely move start to the next!
                total = 0;
            }
        });
        start as i32
    }
}
