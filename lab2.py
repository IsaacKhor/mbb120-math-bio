import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from functools import partial
import lib

wild_log_model = partial(lib.log_dif_model, 0.78056597, 0.34605976)
mut_log_model = partial(lib.log_dif_model, 0.67301681, 0.23029056)

with open('lab1/Purdy_lab_dataset2.txt') as f:
    data = np.array([x.strip().split(',') for x in f.readlines()]).transpose()
    wild_data = [float(x) for x in data[0]]
    mut_data = [float(x) for x in data[1]]

wild_rick_model = partial(lib.ricker_dif_model, 0.39, 0.34605976)
mut_rick_model = partial(lib.ricker_dif_model, 0.335, 0.23029056)

wild_rick_model_data = lib.gen_data(wild_rick_model, wild_data[0], 39)
mut_rick_model_data = lib.gen_data(mut_rick_model, mut_data[0], 39)

time = np.linspace(0,19,39)

plt.figure()
plt.plot(time, wild_rick_model_data, 'g-')
plt.plot(time, wild_data, 'bo')
plt.title('Wild-type model')
plt.savefig('wild_model.png')

plt.figure()
plt.plot(time, mut_rick_model_data, 'g-')
plt.plot(time, mut_data, 'bo')
plt.title('Mutant-type model')
plt.savefig('mut_model.png')

plt.figure()
lib.plt_cobweb(wild_rick_model, wild_data[0], xmax=0.35, title="Wild-type cobweb", xlabel="Population at time t", ylabel="Population at time t+1")
plt.savefig('wild_cobweb.png')

plt.figure()
lib.plt_cobweb(mut_rick_model, mut_data[0], xmax=0.25, title="Mutant-type cobweb", xlabel="Population at time t", ylabel="Population at time t+1")
plt.savefig('mut_cobweb.png')