# ackley.py

import numpy as np

def ackley(x, a=20, b=0.2, c=2 * np.pi):
    """
    Funkcja Ackleya w n-wymiarach.
    x – lista lub wektor numpy o długości n.
    """
    x = np.array(x)
    n = x.size
    sum_sq_term = -a * np.exp(-b * np.sqrt(np.sum(x**2) / n))
    cos_term    = -np.exp(np.sum(np.cos(c * x)) / n)
    return sum_sq_term + cos_term + a + np.exp(1)
