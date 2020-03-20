class Solution {
public:
  int countNumbersWithUniqueDigits(int n);
};

//f 0 = 1
//f 1 = 10
//f 2 = 91
//f n | n > 10 = f 10
//f n = (f (n-1) - f (n-2)) * (10 - n + 2) + f (n-2)
int Solution::countNumbersWithUniqueDigits(int n) {
  if(n == 0) return 1;
  if(n == 1) return 10;
  
  int a = 1, b = 10, c = 0;
  for(int i(2); i <= n; ++i)
    c = (b - a) * (10 - i + 2) + a,
    a = b, b = c;
  return b;
}


