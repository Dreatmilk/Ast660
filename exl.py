import numpy as np

uplim = 100.
lowlim = 201.

narr = np.arange(uplim, lowlim, 1.)
M = max(narr)
m = min(narr)
x = 0.
for index, var in enumerate(narr):
  x += var
print("Summation from", m, "to", M, "=", x)
