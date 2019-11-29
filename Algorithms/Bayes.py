from functools import reduce
import numpy as np


def p(data, X, x, Y, y, con = None):
  "Computes P(X|Y)"
  d = data[data[:, Y] == y]
  if not con:
    b = d[d[:, X] == x]
    return len(b) / len(d)
  else:
    #mean = d[:, X].sum() / len(d)
    #std  = sum([(e - mean)**2 for e in d[:, X]]) / len(d)
    #m = np.exp(-((x-mean)**2/2*std))
    #r = (1/((np.sqrt(2*np.pi))*np.sqrt(std))) * np.exp(-((x-mean)**2/2*std))
    #print(con, mean, std, r)
    dis = np.floor(d[:, X])
    b = dis[dis == np.floor(x)]
    return len(b) / len(d)
  #end

def prob(data, x, Y, y, cons):
  return reduce(lambda a, e: a * e, [p(data, i+1, x[i], Y, y, cons[i+1]) for i in range(0, len(x)-1)])
  #end

def poss(data, Y, y, con = None):
  return len(data[data[:, Y] == y]) / len(data)
  #end
  
def bayes(data, cons):
  """
  The main Bayes function
  * Input:
    + data: The main data, need to be a matrix with type being the 1st column
    + cons: The list to indicate whether the corresponding feature is continuous
  * Return: the classifier function
  """
  def classifier(x):
    types = np.unique(data[:, 0])
    ps = [poss(data, 0, t) * prob(data, x, 0, t, cons) for t in types]
    #print(ps)
    t = types[ps.index(max(ps))]
    return t
    #end
  return classifier
  #end


def test(data):
  r = p(data, 1, 1, 0, 0)
  print(r)
  #end


def train(data):
  #tt = {'Iris-setosa': 1, 'Iris-versicolor': 0, 'Iris-virginica': 1}
  #x = data[:, 0]
  #data[:, 0] = np.array(list(map(lambda e: tt[e], x)))

  f = bayes(data, [False, True, True, True, True])
  ok = 0
  for e in data:
    t = f(e[1:])

    ok = ok + (1 if t == e[0] else 0)
    print(">" if t == e[0] else " ", end = "")#+ ": " + str(r) + " =/= " + str(e[0]))
    #break
    #end for
  print()
  print("Train ratio: " + str(ok / len(data)))
  return f
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





