"""
The main test module!
* Algorithms:
  + Decision Tree
  + Neural network
  + Naive Bayes
  + ...
"""

from Data import *       
import DecisionTree as dt
import Perception   as nn
import Bayes        as by

DecisionTree  = 0
NeuralNetwork = 1
NaiveBayes    = 2


def test(kind):
  No = [O_0, T_T, Q_Q]
  return No[kind]
  #end

def O_0(data, n):
  "Decision Tree"
  print("Testing Decision Tree...")
  r = crossValid(dt.train, dt.valid, data, n)
  print("\nFinal ratio: " + str(r))
  #end

def T_T(data, n):
  "Neural network"
  print("Testing Neural network...")
  r = crossValid(nn.train, nn.valid, data, n)
  print("\nFinal ratio: " + str(r))
  #end

def Q_Q(data, n):
  "Naive Bayes"
  r = crossValid(by.train, by.valid, data, n)
  print("\nFinal ratio: " + str(r))
  #end




  

