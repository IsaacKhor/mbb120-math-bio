import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from functools import partial

def expModel(init, x, rate):
    return init * (x ** rate)

def logModel(init, x, rate, carryingCap):
    num = init * np.exp(rate*x)
    dem = 1 + (init/carryingCap)*(np.exp(rate*x)-1)
    return num/dem

with open("lab1/Purdy_lab_dataset2.txt") as f:
     content = [x.strip().split(',') for x in f.readlines()]

data = np.array(content).transpose()
mutData = data[0]
wildData = data[1]
time = np.linspace(0,19,39)
mutExpModel = partial(expModel, mutData[0])
wildExpModel = partial(expModel, wildData[0])
mutLogModel = partial(logModel, mutData[0])
wildLogModel = partial(logModel, wildData[0])

print(wildData, time)

wildOpt, wildExpCov = opt.curve_fit(wildExpModel, time[0:20], wildData[0:20])
print(wildOpt, np.sqrt(np.diag(wildExpCov)))