class Solution {
public:
  int nthUglyNumber(int n);
  int nthUglyNumber_hack(int n);
};

//f 1 = 1
//f n = min $ map f [1..(n-1)] >>= \i -> [i*2, i*3, i*5]
//However, we don't need to check each ungly number we have generated,
//instead, we want to record which numbers do not need to check again.
//Therefore, we use 3 record pointers(a, b, c) to decrease compilexity.
int Solution::nthUglyNumber(int n) {
  int a = 0, b = 0, c = 0;
  vector<int> rc(n, 1);
  for(int i = 1; i < n; i++) {
    int cur = min(rc[a] * 2, min(rc[b] * 3, rc[c] * 5));
    if (rc[a] * 2 == cur) a++;
    if (rc[b] * 3 == cur) b++;
    if (rc[c] * 5 == cur) c++;
    rc[i] = cur;
  }
  return rc[n - 1];
}


//(This is just alittle hack, not practical but interesting ;-)
int Solution::nthUglyNumber_hack(int n) {
  
  static vector<int> u_nums;
  if (u_nums.empty()){
    for (long a = 1; a <= INT_MAX; a *= 2)
      for (long b = a; b <= INT_MAX; b *= 3)
        for (long c = b; c <= INT_MAX; c *= 5)
          u_nums.push_back(c);
 
    sort(u_nums.begin(), u_nums.end());           
  }
  return u_nums[n-1];
}




