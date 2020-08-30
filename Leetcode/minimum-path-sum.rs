use std::collections::HashMap;

impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let I = grid.len() - 1;
        let J = grid[0].len() - 1;

        let mut rc = vec![0; J + 1];
        for i in (0..I+1).rev() {
            for j in (0..J+1).rev() {
                if i == I && j == J {
                    rc[j] = grid[i][j];
                    continue;
                }
                let down = if i + 1 <= I {
                    rc[j]
                } else {-1};
                let right = if j + 1 <= J {
                    rc[j+1]
                } else {-1};
                rc[j] = (if down == -1 || right == -1 {
                    down.max(right)
                } else {
                    down.min(right)
                }) + grid[i][j];
            }
        }
        rc[0]
    }
    pub fn min_path_sum_recursive(grid: Vec<Vec<i32>>) -> i32 {
        fn min_path(
            grid: &Vec<Vec<i32>>,
            i: usize, j: usize, I: usize, J: usize,
            rc: &mut HashMap<(usize, usize), i32>
        ) -> i32 {
            if i == I && j == J {
                return grid[i][j];
            }
            if let Some(cnt) = rc.get(&(i, j)) {
                return *cnt;
            }
            let down = if i + 1 <= I {
                min_path(grid, i+1, j, I, J, rc)
            } else {
                -1
            };
            let right = if j + 1 <= J {
                min_path(grid, i, j+1, I, J, rc)
            } else {
                -1
            };
            let ans = (if down == -1 || right == -1 {
                down.max(right)
            } else {
                down.min(right)
            }) + grid[i][j];

            rc.insert((i, j), ans);
            ans
        }
        let mut rc = HashMap::new();
        let ans = min_path(&grid, 0, 0, grid.len()-1, grid[0].len()-1, &mut rc);
        ans
    }
}
