from Transfer import *


class Perception:
  "Simple perception"
  
  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.w = np.empty((m, n))
    self.b = 0
    #end
  
  def a(self, x):
    return np.dot(self.w, x) + self.b
    #end
  
  def forward(self, x):
    return hardlim(self.a(x))
    #end
  
  def error(self, x, y):
    return y - self.forward(x)
    #end
  
  def loss(self, x, y) -> float:
    return (self.error(x, y) ** 2).sum()
    #end
  
  def update(self, x, y):
    e = self.error(x, y)
    self.w = self.w + e * x
    self.b = self.b + e
    #end

  def correct(self, x, y):
    return (self.forward(x) == y).sum() / len(y.T)
    #end
  
  def train(self, x, y):
    step = 0
    while ((not (self.error(x, y) == 0).all())
         and self.correct(x, y) < 0.9
         and step < 1000):
      i = step % len(x.T)
      self.update(x[:, i], y[:, i])
      step += 1
      print(str(step) + ":\tLoss: " + str(self.loss(x, y)))
      print("Ratio: " + str((self.forward(x) == y).sum() / len(y.T)))
      print(self.correct(x, y))
      #end while
    #end

  def __call__(self):
    return self.forward
    #end
  
  #end class Perception



def train(data):
  x = data[:, 1:].T
  y = data[:, 0]
  """
  There are 3 types:
  ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
  """
  """
  Firstly, let's distinguish the first 2 types:
  ['Iris-setosa', 'Iris-versicolor']
  [0            , 1                ]
  """
  view = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 1}
  y0 = np.array([list(map(lambda t: view[t], y))])
  nn0 = Perception(1, 4)
  nn0.train(x, y0)

  print("----------------------------------------")
  view = {'Iris-setosa': 0, 'Iris-versicolor': 0, 'Iris-virginica': 1}
  y1 = list(map(lambda t: view[t], y))
  nn1 = Perception(1, 4)
  nn1.train(x, np.array([y1]))

  def classifier(x):
    a = nn0()(x)
    b = nn1()(x)
    if a == 0: return 'Iris-setosa'
    if b == 0: return 'Iris-versicolor'
    return 'Iris-virginica'
    #end
  ok = 0
  for e in data:
    t = classifier(e[1:])
    ok = ok + (1 if t == e[0] else 0)
    print(">" if t == e[0] else " ", end = "")#+ ": " + str(r) + " =/= " + str(e[0]))
    #end for
  print()
  print("Train ratio: " + str(ok / len(data)))
  return classifier
  #end


def valid(f, data):
  ok = 0
  for e in data:
    # print(e[1:])
    r = f(e[1:])
    ok = ok + (1 if r == e[0] else 0)
    #print(">", end = "")
    print(">" if r == e[0] else " ", end = "")#+ ": " + str(r) + " =/= " + str(e[0]))

  print()
  print("Valid ratio: " + str(ok/len(data)))
  return ok/len(data)
  #end
  


