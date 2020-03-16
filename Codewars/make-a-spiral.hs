module Spiral where

spiralize :: Int -> [[Int]]
spiralize 4 = 
  [[1,1,1,1],
   [0,0,0,1],
   [1,0,0,1],
   [1,1,1,1]]
spiralize 3 = 
  [[1,1,1],
   [0,0,1],
   [1,1,1]]
spiralize 2 =
  [[1,1],
   [0,1]]
spiralize 1 =
  [[1]]
spiralize n = 
  let (x:xs) = spiralize (n-4) in
  map (const 1) [1..n] 
  : (map (const 0) [2..n] ++ [1]) 
  : (1 : 1 : x ++ [0, 1]) 
  : map (\e -> 1 : 0 : e ++ [0, 1]) xs 
  ++ [[1, 0] ++ map (const 0) [5..n] ++ [0, 1]] 
  ++ [map (const 1) [1..n]]
