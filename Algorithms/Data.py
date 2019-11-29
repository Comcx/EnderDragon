import matplotlib.pyplot as plt
import copy
import numpy as np
import pandas as pd

# IO
iris = pd.read_csv('iris.data')

# Tags
iris.columns = ['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'class']

class Iris:

  frame = iris
  value = np.concatenate((np.array([frame.values[:, -1].T]),
                          np.array(frame.values[:, 0:-1].T))).T   
  def __init__(self, data):
    self.frame = self.__class__.frame
    self.data = data
    #end

  def show(self):
    print(self.frame)
    print(self.frame.describe())

  def shuffle(self, n = None):
    n = n or len(self.data)
    ans = copy.deepcopy(self.data)
    for time in range(n):
      i = int(np.floor(np.random.rand(1) * len(ans)))
      j = int(np.floor(np.random.rand(1) * len(ans)))
      t = ans[j].copy()
      ans[j] = ans[i]
      ans[i] = t
      #end for
    return self.__class__(ans)
    #end


def crossValid(train, valid, data, div):
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
    log.append(valid(t, data_valid))
    #end for
  print("Cross ratios: " + str(log))
  return sum(log) / div
  #end


data = Iris(Iris.value)



    
