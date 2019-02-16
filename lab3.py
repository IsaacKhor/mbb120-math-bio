import numpy as np
import matplotlib.pyplot as plt

r = 1
m = np.array(
# Seed, Veg, Male, Fem
[[0.86, 0,    0,    r],     # Seedling
 [0.14, 0.35, 0.18, 0.06],  # Vegetative
 [0,    0.41, 0.72, 0.13],  # Male
 [0,    0.14, 0.08, 0.62]]) # Female

def get_model(rate):
    ret = m.copy()
    ret[0,3] = rate
    return ret

init = np.array([15, 20, 201, 68])

def simulate(init_vec, model, iterations):
    ret = [0]*iterations
    last_vec = init_vec.T
    for i in range(iterations):
        ret[i] = last_vec
        last_vec = model.dot(last_vec)
    ret = np.array([x.transpose() for x in ret])
    return ret

time = np.linspace(0,49,50)

def plot_structured_data(init, rate, filename):
    model = get_model(rate)
    data = simulate(init, model, 50).transpose()

    plt.figure()
    plt.plot(time, data[0], 'k-', label="Seedling")
    plt.plot(time, data[1], 'g-', label="Vegetative")
    plt.plot(time, data[2], 'b-', label="Male")
    plt.plot(time, data[3], 'r-', label="Female")
    plt.xlabel("Time")
    plt.ylabel("Population of trees")
    plt.title("Model with tau=" + str(rate))
    plt.legend()
    plt.savefig(filename)

# plot_structured_data(init, 0.03, "m1.png")
# plot_structured_data(init, 0.3, "m2.png")
# plot_structured_data(init, 1.3, "m3.png")
# plot_structured_data(init, 3, "m4.png")

plot_structured_data(np.array([20, 201, 68, 15]), 1.3, "p1.png")
plot_structured_data(np.array([68, 15, 20, 201]), 1.3, "p2.png")
plot_structured_data(np.array([201, 68, 15, 20]), 1.3, "p3.png")
