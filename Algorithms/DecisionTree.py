from functools import reduce
from scipy import stats
import numpy as np


def compose(*fs):
  return reduce(lambda *a, **kw: f(g(*a, **kw)), fs)
  #end

class DecisionTree:
  """
  * Description: The great class Data which contains all 
    data mining algorithms I need
  * Building: need data being a numpy array, 
    within with the 0 column index is the type
    - e.g. [type 1 2 3 4]
            Y    1 2 3 4
  * Algorithms:
    + Descision Tree
    + Naive Bayes
    + Neural Network
  """
  # Main types of decision trees
  ID3  = 0
  C4_5 = 1
  CART = 2
  def __init__(self, tt, raw, at = None):
    '''
    NOTE! It's your responsibility to make sure that the size of data
          is at least 2 x 2
    '''
    if raw.size == 0:
      #print("Warning: Empty data!")
      #print(raw)
      pass
    self.data  = raw
    self.type  = tt
    self.attrType = at
    self.shape = self.data.shape
    self.empty = self.data.size == 0

    if self.type == self.ID3:
      self.metric = self.__class__.entropy
    elif self.type == self.C4_5:
      self.metric = self.__class__.entropy
    elif self.type == self.CART:
      self.metric = self.__class__.gini
    else:
      self.metric = self.__class__.entropy
      #end if
    #end

  def __len__(self) -> int:
    return len(self.data)
    #end

  def types(self):
    '''
    return array of types
    '''
    return self.data[:, 0] if not self.empty else np.array([])
    #end

  def attrs(self):
    '''
    return array of attributes
    '''
    return range(1, len(self.data[0, :])) if not self.empty else []
    #end

  def discretize(self):
    return self.__class__(
      self.type,
      np.concatenate((np.array([self.data[:, 0].T]), np.array(self.data[:, 1:], dtype=int).T)).T,
      self.attrType)
                      
    #end
      
  def dataOfAttr(self, attr: int, f):
    '''
    Filter data satisfying specific rule f
    '''
    d = self.data[np.where(f(self.data[:, attr]), True, False), :]
    return self.__class__(self.type, d, self.attrType)
    #end
    
  def divide(self, attr, divisor = None):
    '''
    The great dividin function which divide data set as you want!
    NOTE: If you don't provide divisor, just divide element by element
          otherwise, divide by the given divisor
     '''
    if divisor == None:
      return reduce(
        lambda a, e: a + [self.dataOfAttr(attr, lambda x: x == e)],
        np.unique(self.data[:, attr]), [])
    else:
      return [ self.dataOfAttr(attr, lambda x: x <= divisor)
         , self.dataOfAttr(attr, lambda x: x >  divisor) ]
      #end if
    #end
  
  def entropy(self) -> float:
    "Calculating entropy..."
    if len(self) <= 0: return 10
    n = len(self.data)
    def accu(a, e):
      r = len(self.dataOfAttr(0, lambda x: x == e)) / n
      return a - r * np.log2(r)
      #end
    return np.array(reduce(accu, np.unique(self.data[:, 0]), 0))
    #end

  def gini(self) -> float:
    return 0
    #end

  def bestDivisor(self, attr: int) -> float:
    if not self.attrType[attr]: return None
    if self.data.size == 0: return 0
    vals = np.unique(np.sort(self.data[:, attr]))
    ps = []
    for i in range(0, len(vals)-1):
      ps.append((vals[i+1] + vals[i]) / 2)
    ps.append(vals[0])
    #print(vals)
    gains = [self.gain(attr, v) for v in ps]
    
    #print(vals[gains.index(max(gains))])
    #print("of")
    #print(vals)
    #print(gains)
    #ss = (self.divide(attr, vals[gains.index(max(gains))]))
    #print(ss[0].data)
    #print(ss[1].data)
    #print()
    #print()
    
    
    return ps[gains.index(max(gains))]
    #end
    
  def gain(self, attr: int, divisor = None) -> float:
    '''
    Calculating gain:
    Using entropy metric by default
    * Metric options:
      + Entropy
      + Gini
      + Classification error
    '''
    n = len(self)
    return self.metric(self) - reduce(
      lambda a, e: len(e)/n * self.metric(e), self.divide(attr, divisor), 1)
    #end
  
  def ratio(self, attr) -> float:
    return 0
    #end
  
  def decide(self, attrs) -> int:
    "Decide the next node!"
    if attrs == []: return 0
    '''
    UNDERWORK!!
    '''
    f = self.gain if self.type == self.__class__.ID3 else self.gain
    c = [f(a, self.bestDivisor(a)) for a in attrs]
    #print(c)
    return attrs[c.index(max(c))]

  
  def gen(self, attrs, n = None):
    "Generating the tree function"
    #print(n)
    if self.entropy() == 0 or attrs == []:
      if self.empty: return lambda x: None
      t = stats.mode(self.types())[0]
      return lambda x: t[0]
    else:
      attr = self.decide(attrs)
      #print(attr)
      attr_rest = list(filter(lambda e: e != attr, attrs))
      '''
      ss = self.divide(attr, self.bestDivisor(attr))
      print(len(ss[0].data), len(ss[1].data))
      print([s.entropy() for s in ss])
      print(self.entropy())
      print()
      '''
      if self.attrType[attr]:
        dd = self.discretize()
        self.data[:, attr] = dd.data[:, attr]
        #end
      fs = np.array([s.gen(attr_rest) for s in self.divide(attr)])#, self.bestDivisor(attr))])
      def merge(x):
        #print("merge")
        if self.attrType[attr]:
          #f = fs[0 if x[attr-1] <= self.bestDivisor(attr) else 1]
          vs = np.unique(np.floor(self.data[:, attr]))
          d = (vs[0] - x[attr-1])**2
          i = 0
          for id in range(1, len(vs)):
            if (vs[id] - x[attr-1])**2 < d:
              i = id
              d = (vs[id] - x[attr-1])**2
              #end if
            #end for
          f = fs[i]
          #print(x[attr-1], vs[i], vs)
          return f(x)
        else:
          f = fs[np.where(np.unique(self.data[:, attr]) == x[attr-1], True, False)]
          if f.size == 0:
            print("Can not classify: " + str(x) + " with " + str(np.unique(self.data[:, attr])))
            return None
          else: return f[0](x)
          #end if
        #end f
      return merge
      #end if
    #end train
  
  def __call__(self):
    "return the tree function"
    return self.gen(self.attrs(), 0)
    #end

  



def train(data):
  '''
  data = np.array(
    [ [1, 2, 3, 4, 7]
    , [0, 4, 5, 6, 8]
    , [1, 6, 7, 6, 2]
    , [1, 4, 8, 0, 3]
    , [2, 4, 1, 1, 1] ])
  '''
  # Using Entropy as default
  #t = DecisionTree(DecisionTree.C4_5, data, [False, True, True, True, True])
  t = DecisionTree(DecisionTree.C4_5, data, [False, True, True, True, True])
  f = t()

  ok = 0
  no = 0
  for e in t.data:
    # print(e[1:])
    r = f(e[1:])
    ok = ok + (1 if r == e[0] else 0)
    #print(">", end = "")
    print(">" if r == e[0] else " ", end = "")#+ ": " + str(r) + " =/= " + str(e[0]))
  print()
  print("Train ratio: " + str(ok/len(t)))
    
  return t
  #end train
  

def valid(t, data):
  f = t()

  ok = 0
  no = 0
  for e in data:
    # print(e[1:])
    r = f(e[1:])
    ok = ok + (1 if r == e[0] else 0)
    #print(">", end = "")
    print(">" if r == e[0] else " ", end = "")#+ ": " + str(r) + " =/= " + str(e[0]))

  print()
  print("Valid ratio: " + str(ok/len(data)))
  return ok/len(data)
  #end test




def _valid(data, div):
  if div <= 1:
    print("The cross time need > 1:)")
    return None
    #end if
  log = []
  n = len(data)
  m = int(len(data) / div)
  for i in range(div):
    print("\n>>Round " + str(i) + ":")
    data_valid = data[i*m : i*m+m]
    data_train = np.concatenate((data[0:i*m], data[i*m+m+1 : n]))
    t = train(data_train)
    log.append(test(t, data_valid))
    #end for
  print("Cross ratios: " + str(log))
  return sum(log) / div
  
  #end


  
  
