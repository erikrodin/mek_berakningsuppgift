# %% Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# %% Define derivative function
def f(t, y):
    dydt = [y[2], y[3], y[1]-2*y[0], y[0]-2*y[1]]
    return dydt
# %% Define time spans, initial values, and constants

tspan = np.linspace(0, 10, 100)
yinit = [1, 0, -1, 0]
# %% Solve differential equation
sol = solve_ivp(lambda t, y: f(t, y),
[tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)
# %% Plot states
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i])
plt.show(block=True)
