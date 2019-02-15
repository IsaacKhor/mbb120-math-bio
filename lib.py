import matplotlib.pyplot as plt
import numpy as np

def plt_cobweb(func, init, **kwargs):
    iterations = kwargs.get('iterations', 40)
    xmax = kwargs.get('xmax', 20)
    title = kwargs.get('title', "Cobweb Plot")
    xlabel = kwargs.get('xlabel', None)
    ylabel = kwargs.get('ylabel', None)

    x = np.linspace(0, xmax, iterations)

    # PLot y=x
    plt.plot(x, x, color="black")

    # Plot the curve
    plt.plot(x, func(x), color="blue")

    # Plot the cobweb
    last_x, last_y = init, 0
    for _ in range(iterations):
        next_x = func(last_x)
        plt.plot([last_x, last_x], [last_y, next_x], color="red")
        plt.plot([last_x, next_x], [next_x, next_x], color="red")
        last_x, last_y = next_x, next_x

    plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)

def gen_data(func, init, iterations):
    last_val = init
    ret = [0] * iterations
    for i in range(iterations):
        ret[i] = last_val
        last_val = func(last_val)
    return ret

def log_dif_model(rate, cap, x):
    return x * (1 + rate * (1 - x/cap))

def ricker_dif_model(rate, cap, x):
    return x * np.exp(rate * (1 - x/cap))
