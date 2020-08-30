use std::collections::HashMap;

impl Solution {
    pub fn unique_paths_with_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        if grid.len() == 0 {
            return 0;
        }
        let M = grid.len();
        let N = grid[0].len();
        if grid[0][0] == 1 || grid[M-1][N-1] == 1{
            return 0;
        }
        let mut rc = vec![0; N+1];
        for i in (0..M).rev() {
            for j in (0..N).rev() {
                rc[j] = if i == M - 1 && j == N - 1 {
                    1
                } else if grid[i][j] == 1 {
                    0
                } else {
                    rc[j] + rc[j+1]
                };
            }
        }
        rc[0]
    }
    pub fn unique_paths_with_obstacles_recursive(grid: Vec<Vec<i32>>) -> i32 {
        fn paths(
            grid: &Vec<Vec<i32>>,
            i: usize, j: usize, I: usize, J: usize,
            rc: &mut HashMap<(usize, usize), usize>
        ) -> usize {
            if i == I && j == J {
                return 1;
            }
            if i > I || j > J {
                return 0;
            }
            if let Some(cnt) = rc.get(&(i, j)) {
                return *cnt;
            }
            let ans = (if i + 1 <= I && grid[i+1][j] == 0 {
                    paths(grid, i+1, j, I, J, rc) } else {0}) +
                if j + 1 <= J && grid[i][j+1] == 0 {
                    paths(grid, i, j+1, I, J, rc) } else {0};
            rc.insert((i, j), ans);
            ans
        }
        if grid.len() == 0 {
            return 0;
        }
        if grid[0][0] == 1 {
            return 0;
        }
        let mut rc = HashMap::new();
        let ans = paths(&grid, 0, 0, grid.len()-1, grid[0].len()-1, &mut rc) as i32;
        ans
    }
}
