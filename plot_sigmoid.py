import numpy as np
import sympy as sp

x = sp.symbols('x')
sp.plotting.plot(1.0 / (1 + np.exp(-x)))
