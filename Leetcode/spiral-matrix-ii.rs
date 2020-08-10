impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        fn gen(i: i32, n: i32) -> Vec<Vec<i32>> {
            if n == 1 {
                return vec![vec![i]];
            }
            if n == 2 {
                return vec![vec![i, i+1], vec![i+3, i+2]];
            }
            let N = n as usize;
            let inner = gen(i+4*n-4, n-2);
            let mut spiral = vec![vec![0; N]; N];
            for j in 1..N-1 {
                spiral[j][0] = i+n*2-1+(n-2)*2 - (j as i32)+1;
                spiral[j][N-1] = i+n+(j as i32)-1;
                for k in 1..N-1 {
                    spiral[j][k] = inner[j-1][k-1];
                }
            }
            spiral[0] = (i..i+n).collect();
            spiral[N-1] = (i+2*n-2 .. i+3*n-2).rev().collect();
            spiral
        }
        gen(1, n)
    }
}
/*
1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7
*/
