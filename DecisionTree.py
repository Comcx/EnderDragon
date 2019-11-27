from functools import reduce
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
  def __init__(self, tt, raw):
    '''
    NOTE! It's your responsibility to make sure that the size of data
          is at least 2 x 2
    '''
    if raw.size == 0:
      print("Warning: Empty data!")
    self.data  = raw
    self.type  = tt
    self.shape = self.data.shape
    self.empty = self.data.size == 0
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
    
  def dataOfAttr(self, attr: int, f):
    '''
    Filter data satisfying specific rule f
    '''
    d = self.data[np.where(f(self.data[:, attr]), True, False), :]
    return self.__class__(self.type, d)
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
    n = len(self.data[:, 0])
    def accu(a, e):
      r = len(self.dataOfAttr(0, lambda x: x == e)) / n
      return a - r * np.log2(r)
      #end
    return np.array(reduce(accu, np.unique(self.data[:, 0]), 0))
    #end

  def gini(self) -> float:
    return 0
    #end

  def bestDivisor(self, attr) -> float:
    vals = np.unique(np.sort(self.data[:, attr]))
    return 0
    #end
    
  def gain(self, attr: int, metric = None) -> float:
    '''
    Calculating gain:
    Using entropy metric by default
    * Metric options:
      + Entropy
      + Gini
      + Classification error
    '''
    if metric == None: metric = self.__class__.entropy
    n = len(self)
    return metric(self) - reduce(
      lambda a, e: len(e)/n * metric(e), self.divide(attr), 0)
    #end

  def ratio(self, attr, metric = None) -> float:
    return 0
    #end

  def decide(self, attrs, metric = None) -> int:
    "Decide the next node!"
    if attrs == []: return 0
    '''
    UNDERWORK!!
    '''
    f = self.gain if self.type == self.__class__.ID3 else self.gain
    c = [f(a, metric) for a in attrs]
    return attrs[c.index(max(c))]
  
  def train(self, attrs, metric = None):
    "Generating the tree function"
    if self.entropy() == 0 or attrs == []:
      t = self.types()[0]
      return lambda x: t
    else:
      attr = self.decide(attrs)
      attr_rest = list(filter(lambda e: e != attr, attrs))
      fs = np.array([s.train(attr_rest, metric) for s in self.divide(attr)])
      def g(x):
        return fs[np.where(np.unique(self.data[:, attr]) == x[0], True, False)][0](x[1:])
        #end
      return g
      #end if
    #end
  
  def __call__(self, metric = None):
    "return the tree function"
    return self.train(self.attrs(), metric)
    #end





data = np.array(
  [ [1, 2, 3, 4, 7]
  , [0, 4, 5, 6, 8]
  , [1, 6, 7, 6, 2]
  , [1, 4, 8, 0, 3]
  , [2, 4, 1, 1, 1] ])

# Using Entropy as default
f = DecisionTree(DecisionTree.C4_5, data)()

for e in data:
  t = f(e[1:])
  print("OK" if t == e[0] else "NO")

#end main

