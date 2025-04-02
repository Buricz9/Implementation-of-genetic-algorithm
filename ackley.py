import numpy as np

def ackley(x, a=20, b=0.2, c=2 * np.pi):
    n = len(x)
    sum_sq_term = -a * np.exp(-b * np.sqrt(np.sum(np.square(x)) / n))
    cos_term = -np.exp(np.sum(np.cos(c * np.array(x))) / n)
    return sum_sq_term + cos_term + a + np.exp(1)

