# %% Imports
from cmath import sin
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# %% Define derivative function
def f(t, y, l, w, m, a):
    dydt = [y[1], y[0]*(g-a*w*w*sin(w*t))/l]
    return dydt
# %% Define time spans, initial values, and constants

g = 9.82 #m/s^2
l = [1, 10] #pendulum lenghts, m
w = [10, 70, 150] #different_frequencies, 1/s
m = 1 #mass, kg
a = 0.1 #amplitude, meter
tspan = np.linspace(0, 10, 100) #timeinterval
yinit = [5, 0] #initial conditions for thetha(0) & thetha´(0)

for i in w:
    for j in l:
        # %% Solve differential equation
        sol = solve_ivp(lambda t, y: f(t, y, j, i, m, a),
        [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)
        # %% Plot states
        for p in range(sol.y.shape[0]):
            plt.plot(sol.t, sol.y[0])
        
    
plt.ylim([-90,90])
plt.show(block=True)
