class Solution {
public:
  int numDecodings(string s);
};

//f (I-1) = if s(I-1) == '0' then 0 else 1
//f i = if s(i) > '2' then f (i+1) 
//      else if s(i) == '2' && s(i+1) <= 6 then f (i+1) + f (i+2)
//      else if s(i) == '1' then f (i+1) + f (i+2)
//      else if s(i) == '0' then 0
//      else f (i+1)
int Solution::numDecodings(string s) {
  if(s.empty())     return 0;
  if(s.size() == 1) return s[0] == '0' ? 0 : 1;
  
  int I = s.size();
  int i1 = s[I-1] == '0' ? 0 : 1, i2 = 1;
  for(int i(I-2); i >=0; --i) {
    int i0 = 0;
    i0 = s[i] >  '2'                 ? i1      :
         s[i] == '2' && s[i+1] < '7' ? i1 + i2 :
         s[i] == '1'                 ? i1 + i2 :
         s[i] == '0'                 ? 0       :
         i1                                    ;
    i2 = i1, i1 = i0;
  }
  return i1;
}




