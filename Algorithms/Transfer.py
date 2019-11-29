from Neura import *

def sigmoid(e):
  "Sigmoid function"
  return 1 / (1 + np.exp(-e))
  #end

def hardlim(e):
  "Hard limit function"
  return np.where(e < 0, 0, 1)
  #end

def symHardlim(e):
  "Symmetrical Hard Lime"
  return np.where(e < 0, -1, 1)
  #end

def linear(e):
  "Pure Linear"
  return e
  #end

def tanSigmoid(e):
  "Hyperbolic Tangent Sigmoid"
  return (np.exp(e) - np.exp(-e)) / (np.exp(e) + np.exp(-e))
  #end

def posLinear(e):
  "Positive Linear"
  return np.where(e < 0, 0, e)
  #end

